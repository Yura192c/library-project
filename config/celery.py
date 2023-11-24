from celery import Celery
import os


app = Celery('config',
             broker=os.environ.get("CELERY_BROKER", 'redis://redis:redis@redis:6379/0'),
             backend=os.environ.get("CELERY_BACKEND", 'redis://redis:redis@redis:6379/0'),
             )
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


@app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
