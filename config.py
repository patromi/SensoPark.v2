import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = 'h'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = int(os.environ.get('MAIL_PORT', '587'))
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    MAIL_SUBJECT_PREFIX = 'SensoPark'
    MAIL_SENDER = 'Serwis SensoPark'
    ADMIN = os.environ.get('FLASKY_ADMIN')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CAPTCHA_ENABLE = True
    CAPTCHA_LENGTH = 5
    CAPTCHA_WIDTH = 160
    CAPTCHA_HEIGHT = 60
    SESSION_TYPE = 'sqlalchemy'

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://bazadanych:Pa2H8vrz3h4PfFNO@34.107.97.144/Sensopark'


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://bazadanych:Pa2H8vrz3h4PfFNO@34.107.97.144/Sensopark'


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://bazadanych:Pa2H8vrz3h4PfFNO@34.107.97.144/Sensopark'


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
