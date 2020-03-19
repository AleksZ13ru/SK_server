from datetime import datetime

from django.db import models
from django.conf import settings
from machines.models import Machine, Developer


class Event(models.Model):
    class Meta:
        verbose_name = "Ремонт"
        verbose_name_plural = "Ремонты"

    machine = models.ForeignKey('machines.Machine', related_name='events', on_delete=models.CASCADE)
    text = models.TextField()
    # comment = models.TextField()
    services = models.ManyToManyField(Developer, related_name='developers')  # Json список вызванных служб
    posted_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)

    def __str__(self):
        text = self.text
        if len(self.text) > 20:
            text = self.text[:20] + '...'
        return '{} | {}'.format(self.machine, text)


class Status(models.Model):
    class Meta:
        verbose_name = "Действие с ремонтом"
        verbose_name_plural = "Действия с ремонтами"

    event = models.ForeignKey('events.Event', related_name='statuses', on_delete=models.CASCADE)
    text = models.TextField()
    comment = models.TextField()
    # status_datetime = models.DateTimeField(default=datetime.now)
    posted_datetime = models.DateTimeField(default=datetime.now)
    posted_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)
