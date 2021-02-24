# Generated by Django 3.1.6 on 2021-02-05 02:52

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0004_auto_20210205_0518'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='endsession',
            name='comment',
        ),
        migrations.AlterField(
            model_name='profile',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 2, 5, 2, 52, 57, 727780, tzinfo=utc), verbose_name='Дата приёма на работу'),
        ),
        migrations.AlterField(
            model_name='session',
            name='endTime',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 5, 2, 52, 57, 729774, tzinfo=utc), verbose_name='Время закрытия смены'),
        ),
        migrations.AlterField(
            model_name='session',
            name='startTime',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 5, 2, 52, 57, 729774, tzinfo=utc), verbose_name='Время открытия смены'),
        ),
    ]
