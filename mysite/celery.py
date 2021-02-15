from __future__ import absolute_import

import os

from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

app = Celery('mysite',
             broker='amqp://guest@localhost//',
             backend='rpc://',
             include=['mysite.tasks']
             )

app.conf.update(result_expires=3600,)


app.config_from_object('django.conf:settings', namespace='CELERY')


app.autodiscover_tasks()