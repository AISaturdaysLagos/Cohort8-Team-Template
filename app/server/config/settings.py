class BaseConfig():
   API_PREFIX = '/api'
   TESTING = False
   DEBUG = False


class DevelopmentConfig(BaseConfig):
   FLASK_ENV = 'development'
   DEBUG = True
   DATABASE_URI = 'postgresql://db_user:db_password@db-postgres:5432/flask-deploy'
   CORS_ALLOWED_ORIGINS="*"


class ProductionConfig(BaseConfig):
   FLASK_ENV = 'production'
   DATABASE_URI = 'postgresql://db_user:db_password@db-postgres:5432/flask-deploy'
   CORS_ALLOWED_ORIGINS="*"


class TestConfig(BaseConfig):
   FLASK_ENV = 'development'
   CORS_ALLOWED_ORIGINS="*"
   TESTING = True
   DEBUG = True