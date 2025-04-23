from .methods import send_notification
from huey.contrib.djhuey import task
import time

@task()
def task_send_notification(message):
    time.sleep(7)
    send_notification(message)