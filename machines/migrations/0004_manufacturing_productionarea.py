# Generated by Django 3.0.4 on 2020-03-19 12:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('machines', '0003_developer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Manufacturing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=120)),
            ],
            options={
                'verbose_name': 'Цех',
                'verbose_name_plural': 'Цеха',
            },
        ),
        migrations.CreateModel(
            name='ProductionArea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=120)),
                ('manufacturing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='manufacturing', to='machines.Manufacturing')),
            ],
            options={
                'verbose_name': 'Участок',
                'verbose_name_plural': 'Участки',
            },
        ),
    ]
