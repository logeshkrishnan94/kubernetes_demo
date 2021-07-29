from __future__ import absolute_import
from celery import Celery
import time
import os


CELERY_BROKER_URL = os.getenv('CELERY_BROKER_URL') if os.getenv('CELERY_BROKER_URL') else 'amqp://'
CELERY_RESULT_BACKEND = os.getenv('CELERY_RESULT_BACKEND') if os.getenv('CELERY_RESULT_BACKEND') else 'redis://'

app = Celery('tasks', broker=CELERY_BROKER_URL, backend=CELERY_RESULT_BACKEND)

@app.task(name='tasks.add')
def add(x,y):
    time.sleep(5)
    return x + y
