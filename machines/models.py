from django.db import models


class Machine(models.Model):
    name = models.TextField(blank=True)
    comment = models.TextField(blank=True)

