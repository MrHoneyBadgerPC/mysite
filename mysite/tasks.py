# Create tasks here

from celery import Celery
from celery import shared_task

app = Celery('tasks', broker='pyamqp://guest@localhost//', backend='amqp')

@app.task(bind=True)
def debug_task(self):
    print(f'Request:{self.request!r}')

@app.task
def add(x, y):
    return x + y

@shared_task
def mul(x, y):
    return x * y

@shared_task
def xsum(numbers):
    return sum(numbers)
