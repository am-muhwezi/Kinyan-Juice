import os
from decouple import config


BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    pass

class DevConfig(Config):
    pass

class ProdConfig(Config):
    pass

class TestConfig(Config):
    pass

Config_dict = {
    'dev': DevConfig,
    'prod': ProdConfig,
    'test': TestConfig,
}