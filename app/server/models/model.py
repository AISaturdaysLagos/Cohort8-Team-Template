import pickle
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder

def load_data(dir):
    df = pd.read_csv(dir)
    return df

def df_wrangle(df, dtype_convert, OneHot_cols):
    '''
    This function wrangles (cleans) our dataset by correcting datypes and One-Hot
    encoding dpecified columns
    
    Inputs
    df: (dataframe), dataframe to wrangle
    dtype_convert: (dictionary), pairs of column, dtype to convert to
    OneHot_col: (list), columns in the dataframe to One-Hot encode
    
    Output
    df: (dataframe), wrangled (cleaned) dataframe
    '''
    
    # convert datatypes to correct formats
    for col, dtype in dtype_convert.items():
        df[col] = df[col].astype(dtype)
        
    # One_Hot encode neccesary columns
    
    # Initialize the One-Hot Encoder
    encoder = OneHotEncoder()
    
    # One-Hot encode each column
    for col in OneHot_cols:
        # variable to store new column names
        df_col_name = []
        
        # unique values in current column
        vals = df[col].unique()             

        for val in vals:
            # replace spaces in values with underscore
            val = val.replace(' ', '_')
            
            # combine initial column name and current value as new column name
            df_col_name.append(col+'_'+val) 
                                            
        # encode the columns
        encoded_df = pd.DataFrame(encoder.fit_transform(df[[col]]).toarray())
        
        # rename the new columns
        encoded_df.columns = df_col_name
        
        # add new columns to dataframe
        df = df.join(encoded_df)

    # drop the initial columns
    df.drop(OneHot_cols, axis=1, inplace=True)
    
    return df

def data_split(df):
    X = df.drop('diabetes', axis=1)
    y = df['diabetes']

    X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.1,
                                                      random_state=123)
    X_dev, X_test, y_dev, y_test = train_test_split(X_val, y_val, test_size=0.5,
                                                    random_state=123)

    return X_train, X_dev, X_test, y_train, y_dev, y_test

def standardize(data):
    scaler = StandardScaler().fit(data)
    data_scaled = scaler.transform(data)
    return data_scaled, scaler

def preprocess(df, dtype_convert, OneHot_cols):
    df = df_wrangle(df, dtype_convert, OneHot_cols)
    X_train, X_dev, X_test, y_train, y_dev, y_test = data_split(df)
    X_train_scaled, scaler = standardize(X_train)
    return X_train_scaled, X_dev, X_test, y_train, y_dev, y_test, scaler

def build_model(model, X_train, y_train):
    return model.fit(X_train, y_train)

def dump_pickle(name, model):
    with open(name, 'wb') as file:
        pickle.dump(model, file)

def build_and_dump_model(dataset_dir, dtype_convert, OneHot_cols,
                         model, dump_name):
    # Read in dataset
    df = load_data(dataset_dir)

    # preprocess data
    X_train_scaled, _, _, y_train, _, _, _ = preprocess(df, dtype_convert,
                                                        OneHot_cols)

    # build model
    base_model = build_model(model, X_train_scaled, y_train)

    # dump model
    dump_pickle(dump_name, base_model)

build_and_dump_model('../Dataset/diabetes_prediction_dataset.csv', {'age':'int'},
                     ['gender', 'smoking_history'], LogisticRegression(), 'model.pkl')