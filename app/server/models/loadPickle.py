import pickle
import numpy as np

def load_model(model_path):
    with open(model_path, 'rb') as file:
        model = pickle.load(file)
    return model

load_model('/Users/grey/workspaces/Cohort8-Johnson-Sirleaf/app/server/models/random_forest_model.pkl')
print('loaded successfully')