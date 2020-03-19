from django.db import models
import json

DB_DATETIME_FORMAT = '%d/%b/%Y %H:%M:%S'
DB_DATE_FORMAT = '%d/%b/%Y'
DB_DATETIME_Z_FORMAT = '%m/%d/%Y 0:0'
DB_TIME_FORMAT = "%H:%M"


class Developer(models.Model):
    class Meta:
        verbose_name = "Служба"
        verbose_name_plural = "Службы"

    name = models.CharField(max_length=120)
    comment = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    class Meta:
        verbose_name = "Тип"
        verbose_name_plural = "Тип оборудования"

    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Manufacturing(models.Model):
    class Meta:
        verbose_name = "Цех"
        verbose_name_plural = "Цеха"

    name = models.CharField(max_length=120, blank=True)

    def __str__(self):
        return self.name


class ProductionArea(models.Model):
    class Meta:
        verbose_name = "Участок"
        verbose_name_plural = "Участки"

    name = models.CharField(max_length=120, blank=True)
    manufacturing = models.ForeignKey('Manufacturing', related_name='manufacturing', on_delete=models.CASCADE)

    def __str__(self):
        return '{}/{}'.format(self.manufacturing.name, self.name)


class Machine(models.Model):
    class Meta:
        verbose_name = "Оборудование"
        verbose_name_plural = "Оборудования"

    name = models.CharField(max_length=120, blank=True)
    comment = models.CharField(max_length=120, blank=True)
    category = models.ForeignKey('Category', related_name='machines', on_delete=models.CASCADE)
    production_area = models.ForeignKey('ProductionArea', related_name='production_area', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def create_manufacturing(self):
        manufacturing = self.production_area.manufacturing.name
        return manufacturing

    def create_area(self):
        return self.production_area.name


class Value(models.Model):
    class Meta:
        verbose_name = "Значение"
        verbose_name_plural = "Значения"

    machine = models.ForeignKey('Machine', related_name='values', on_delete=models.CASCADE)
    day = models.DateField()
    value = models.TextField(default='[]')
    status = models.TextField(default='[]')

    def __str__(self):
        result = '%s | %s=%d ' % (
            self.day.strftime(DB_DATE_FORMAT),
            self.machine,
            len(json.loads(self.value))
        )
        return result

    def create_kmv(self):
        values = json.loads(self.value)
        return round((len(values) - values.count(0)) / len(values), 2)

    def create_speed(self):
        length = 0
        work_time = 0
        speed = 0
        for s in json.loads(self.value):
            if s > 0:
                work_time = work_time + 1
                length = length + s
        if work_time != 0:
            speed = round(length / work_time, 2)
        return speed
