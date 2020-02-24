from datetime import datetime

from django.db import models
from django.conf import settings
from machines.models import Machine


class Event(models.Model):
    machine = models.ForeignKey('machines.Machine', related_name='events', on_delete=models.CASCADE)
    text = models.TextField()
    # comment = models.TextField()
    service = models.TextField()  # Json список вызванных служб
    posted_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)


class Status(models.Model):
    event = models.ForeignKey('events.Event', related_name='statuses', on_delete=models.CASCADE)
    text = models.TextField()
    comment = models.TextField()
    # status_datetime = models.DateTimeField(default=datetime.now)
    posted_datetime = models.DateTimeField(default=datetime.now)
    posted_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)

