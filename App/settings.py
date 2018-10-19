import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

class BaseConfig():
    DEBUG = True
    TESTING = False
    SECRET_KEY = 'FKADJSK3AUjkejf'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SESSION_TYPE = 'redis'


class DevelopConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = 'sqlite:////' + os.path.join(BASE_DIR,'develop.db')





config = {
    'default':DevelopConfig,
    'develop':DevelopConfig,
}

