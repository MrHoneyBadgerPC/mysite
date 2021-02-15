from __future__ import absolute_import

import os

from django.conf import settings
from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

app = Celery('mysite',
             broker='amqp://guest@localhost//',
             backend='rpc://',
             include=['mysite.tasks']
             )

app.conf.update(result_expires=3600,)

<<<<<<< HEAD
app.config_from_object('django.conf:settings')


app.autodiscover_tasks(settings.INSTALLED_APPS)

@app.task(bind=True)
def debug_task(self):
    print('Request: (0!r)'.format(self.request))
=======

app.config_from_object('django.conf:settings', namespace='CELERY')


app.autodiscover_tasks()
>>>>>>> b9f90b380a7ff55ef83e423acba5405bd8187e5e
