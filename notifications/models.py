from django.db import models

# from notifications.methods import send_notification
from notifications.tasks import task_send_notification

# Create your models here.
class Notification(models.Model):
    message = models.TextField()

    def save(self, *args, **kwargs):
        task_send_notification(self.message)
        super().save(*args, **kwargs)