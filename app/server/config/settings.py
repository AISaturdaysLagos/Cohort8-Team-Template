class BaseConfig():
   API_PREFIX = '/api'
   TESTING = False
   DEBUG = False


class DevelopmentConfig(BaseConfig):
   FLASK_ENV = 'development'
   DEBUG = True
   DATABASE_URI = 'postgresql://db_user:db_password@db-postgres:5432/flask-deploy'
   CORS_ALLOWED_ORIGINS="*"
   CORS_ALLOWED_METHODS="GET,POST,PUT,DELETE,PATCH"
   CORS_ALLOWED_HEADERS='origin,x-requested-with,content-type,accept,authorization'


class ProductionConfig(BaseConfig):
   FLASK_ENV = 'production'
   DATABASE_URI = 'postgresql://db_user:db_password@db-postgres:5432/flask-deploy'
   CORS_ALLOWED_ORIGINS="*"
   CORS_ALLOWED_METHODS="GET,POST,PUT,DELETE,PATCH"
   CORS_ALLOWED_HEADERS='origin,x-requested-with,content-type,accept,authorization'


class TestConfig(BaseConfig):
   FLASK_ENV = 'development'
   CORS_ALLOWED_ORIGINS="*"
   CORS_ALLOWED_METHODS="GET,POST,PUT,DELETE,PATCH"
   CORS_ALLOWED_HEADERS='origin,x-requested-with,content-type,accept,authorization'
   TESTING = True
   DEBUG = True