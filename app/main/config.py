"""Configurations for dev, prod, testing, etc"""

import os

class Config:
    """General config"""

    SECRET_KEY = os.getenv('SECRET_KEY', 'my_precious_secret_key')
    DEBUG = False


class DevelopmentConfig(Config):
    """Config for dev"""

    DEBUG = True


class TestingConfig(Config):
    """Config for testing"""

    DEBUG = True
    TESTING = True
    PRESERVE_CONTEXT_ON_EXCEPTION = False


class ProductionConfig(Config):
    """Config for prod"""

    DEBUG = False


config_by_name = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)

key = Config.SECRET_KEY
