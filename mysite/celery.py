from __future__ import absolute_import

import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

app = Celery('mysite',
             broker='amqp://guest@localhost//',
             backend='amqp://guest@localhost//',
             include=['mysite.tasks']
             )

app.conf.update(
        CELERY_TASK_SERIALIZER = 'json',
        CELERY_RESULT_SERIALIZER = 'json',
        CELERY_ACCEPT_CONTENT = ['json'],
        CELERY_TIMEZONE = 'Europe/London',
        CELERY_ENABLE_UTC = True
                )

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

@app.task(bind=True)
def debug_taski(self):
    print(f'Request:{self.request!r}')
