import os


class Config(object):
    DEBUG = False
    CSRF_ENABLED = True
    SECRET_KEY = os.urandom(32)
    DirectoryData = "data"
    MYSQL_PASSWORD = 'password'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # SQLALCHEMY_ENGINE_OPTIONS={"connect_args": {"options": "-c timezone=utc"}}
    connect_args = {"options": "-c timezone=utc"}
    SQLALCHEMY_DATABASE_URI = 'mysql://root:''@localhost/uesrs'


class DevelopmentConfig(Config):
    """Configurations for Development."""
    DEBUG = True


class TestingConfig(Config):
    """Configurations for Testing, with a separate test database."""
    TESTING = True
    DEBUG = True


class StagingConfig(Config):
    """Configurations for Staging."""
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False
    TESTING = False


app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'staging': StagingConfig,
    'production': ProductionConfig,

}
