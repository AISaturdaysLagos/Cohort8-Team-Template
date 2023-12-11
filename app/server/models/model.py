import pickle
import numpy as np

def load_model(model_path):
    with open(model_path, 'rb') as file:
        model = pickle.load(file)
    return model

def make_prediction(model, input_features):
    input_features = np.array(input_features).reshape(1, -1)
    prediction = model.predict(input_features)
    return prediction[0]

def predict_health_status(gender, age, hypertension, heart_disease, smoking_history, bmi, HbA1c_level, blood_glucose_level):
    """
    Predict health status based on several input features.

    Parameters:
    gender (int): Numerical value for gender (0, 1, 2, etc. - specific encoding needs to be defined).
    age (int): Age in years.
    hypertension (int): 0 if no hypertension, 1 if there is hypertension.
    heart_disease (int): 0 if no heart disease, 1 if there is heart disease.
    smoking_history (int): Numerical representation of smoking history (e.g., 0 for never smoked, 1 for former smoker, etc.).
    bmi (float): Body Mass Index.
    HbA1c_level (float): Hemoglobin A1c level.
    blood_glucose_level (float): Blood glucose level.
    diabetes (int): 0 if no diabetes, 1 if there is diabetes.

    Returns:
    int: The predicted health status (specific encoding of the output needs to be defined).
    """
    model_path = './models/xgboostmodel.pkl'
    model = load_model(model_path)

    input_features = [age, hypertension, heart_disease, bmi, HbA1c_level, blood_glucose_level, gender, smoking_history]
    prediction = make_prediction(model, input_features)
    return prediction

# # Example usage
# prediction = predict_health_status(0, 50, 1, 1, 1, 999.5, 9.7, 200)
# print("Prediction:", prediction)
# prediction = predict_health_status(0, 54, 0, 0, 0, 27.32, 6.6, 80)
# print("Prediction:", prediction)
