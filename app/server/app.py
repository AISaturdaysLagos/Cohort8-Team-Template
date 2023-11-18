import os
from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv

load_dotenv()

import config


app = Flask(__name__)

allowed_origins = config.CORS_ALLOWED_ORIGINS.split(',')
resource_pattern = f"{config.API_PREFIX}/*"

CORS_ALLOWED_ORIGINS = config.CORS_ALLOWED_ORIGINS.split(',')
CORS(app, resources={resource_pattern: {"origins": CORS_ALLOWED_ORIGINS}})


@app.route("/")
def hello():
    return "<h1 style='color:blue'>Hello There!</h1>"

if __name__ == "__main__":
    app.run(host='0.0.0.0')