#!/usr/bin/bash

flask run --host=0.0.0.0 --port=8003&
celery -A src.worker:celery worker --loglevel=INFO&

wait