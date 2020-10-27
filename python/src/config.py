import os

class Config(object):
    DEBUG = False

    BROKER_URL = os.getenv("BROKER_URL", 'redis://redis:6379/0')
    CELERY_RESULT_BACKEND = os.getenv(
        "CELERY_RESULT_BACKEND", 'redis://redis:6379/0'
    )
    CELERY_SEND_SENT_EVENT = True


class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    pass


# return active config
available_configs = dict(development=DevelopmentConfig, production=ProductionConfig)
selected_config = os.getenv("FLASK_ENV", "production")
config = available_configs.get(selected_config, "production")
