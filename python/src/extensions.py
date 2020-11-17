from celery import Celery
celery = Celery()

def register_extensions(app, worker=False):
    # load celery config
    celery.config_from_object(app.config)

    if not worker:
        # register celery irrelevant extensions
        pass