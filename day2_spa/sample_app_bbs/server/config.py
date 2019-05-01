# import os

# # You need to replace the next values with the appropriate values for your configuration

# basedir = os.path.abspath(os.path.dirname(__file__))
# SQLALCHEMY_ECHO = False
# SQLALCHEMY_TRACK_MODIFICATIONS = True
# SQLALCHEMY_DATABASE_URI = "postgresql://username:password@localhost/database_name"

import os


class DevelopmentConfig:

    # basedir = os.path.abspath(os.path.dirname(__file__))

    # Flask
    DEBUG = True

    # SQLAlchemy
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    # print('SQLALCHEMY_DATABASE_URI:', SQLALCHEMY_DATABASE_URI)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False


Config = DevelopmentConfig
