import os
basedir = os.path.abspath(os.path.dirname(__file__))

print("CONFIG READ")

class Config(object):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///shorturl.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True