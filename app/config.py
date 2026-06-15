import os


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY")
    DEBUG = False
    Testing = False


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    Testing = True


# used later for pytest and all


class ProductionConfig(Config):
    DEBUG = False


config_by_name = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig,
}
