import os
from decouple import config
from datetime import timedelta

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY=config('SECRET_KEY', 'secret')
    JWT_SECRET_KEY=config('JWT_SECRET_KEY')
    JWT_ACCESS_TOKEN_EXPIRES=timedelta(minutes=30)
    JWT_REFRESH_TOKEN_EXPIRES=timedelta(minutes=140)
    SQLALCHEMY_TRACK_MODIFICATIONS=False

class DevConfig(Config):
    DEBUG=config('DEBUG', cast=bool)
    SQLALCHEMY_ECHO=True
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    SQLALCHEMY_DATABASE_URI='sqlite:///'+os.path.join(BASE_DIR, 'dev.db')


class ProdConfig(Config):
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    SQLALCHEMY_DATABASE_URI=config('DATABASE_URL')
    DEBUG=config('DEBUG', cast=bool)

class TestConfig(Config):
    TESTING=True
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    DEBUG=config('DEBUG', cast=bool)

Config_dict = {
    'dev': DevConfig,
    'prod': ProdConfig,
    'test': TestConfig,
}