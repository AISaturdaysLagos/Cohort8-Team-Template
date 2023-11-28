import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
from cerberus import Validator

from models.model import predict_health_status

load_dotenv()

import config


app = Flask(__name__)

allowed_origins = config.CORS_ALLOWED_ORIGINS.split(',')

CORS_ALLOWED_ORIGINS = config.CORS_ALLOWED_ORIGINS.split(',')
CORS_ALLOWED_METHODS = config.CORS_ALLOWED_METHODS.split(',')
CORS_ALLOWED_HEADERS = config.CORS_ALLOWED_HEADERS.split(',')
CORS(app, resources={r"/api/*": {"origins": CORS_ALLOWED_ORIGINS, "exposed_headers": CORS_ALLOWED_HEADERS, "allowed_headers": CORS_ALLOWED_HEADERS, "methods": CORS_ALLOWED_METHODS}})


request_schema = {
    "firstName": {"type": "string", "required": True},
    "lastName": {"type": "string", "required": True},
    "gender": {"type": "string", "allowed": ["male", "female"], "required": True},
    "age": {"type": "integer", "required": True},
    "email": {"type": "string", "required": True, "regex": r'\S+@\S+\.\S+'},  # Basic email regex
    "hypertension": {"type": "integer", "allowed": [0, 1], "required": True},
    "heart_disease": {"type": "integer", "allowed": [0, 1], "required": True},
    "diabetes": {"type": "integer", "allowed": [0, 1], "required": True},
    "HbA1c_level": {"type": "number", "required": True},
    "smoking_history": {"type": "string", "allowed": ["not current", "former", "no info", "current", "never and ever"], "required": True},
    "blood_glucose_level": {"type": "number", "required": True},
    "bmi": {"type": "number", "required": True},
}

validator = Validator()


@app.route("/")
def hello():
    return "<h1 style='color:blue'>Hello There!</h1>"

@app.route('/api/diabetic-checker', methods=['POST'])
def validate_and_print():
    data = request.get_json()
    if validator.validate(data, request_schema):
        print("Received valid request data:")
        prediction = predict_health_status(data.gender, data.age, data.hypertension, data.heart_disease, data.smoking_history, data.bmi, data.HbA1c_level, data.blood_glucose_level)
        
        if prediction:
            message = "You are at risk of having diabetes."
        else:
            message = "You are not at risk of having diabetes."
        
        return jsonify({"message": message}), 200
    else:
        return jsonify({"error": "Validation error", "details": validator.errors}), 400

if __name__ == "__main__":
    app.run(host='0.0.0.0')