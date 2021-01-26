# Create tasks here

from celery import Celery
from celery import shared_task

app = Celery('tasks', broker='pyamqp://guest@localhost//', backend='amqp')

@app.task
def add(x, y):
    return x + y

@shared_task
def mul(x, y):
    return x * y

@shared_task
def xsum(numbers):
    return sum(numbers)
