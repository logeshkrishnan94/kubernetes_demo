import os
from celery import Celery


CELERY_BROKER_URL = os.getenv('CELERY_BROKER_URL') if os.getenv('CELERY_BROKER_URL') else 'amqp://'
CELERY_RESULT_BACKEND = os.getenv('CELERY_RESULT_BACKEND') if os.getenv('CELERY_RESULT_BACKEND') else 'redis://'

app = Celery('tasks', broker=CELERY_BROKER_URL, backend=CELERY_RESULT_BACKEND)
