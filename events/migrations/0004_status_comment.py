# Generated by Django 3.0.2 on 2020-02-01 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='status',
            name='comment',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
