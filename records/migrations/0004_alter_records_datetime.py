# Generated by Django 4.2 on 2023-05-02 19:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0003_alter_records_datetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='records',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 2, 19, 29, 15, 931299), verbose_name='Время'),
        ),
    ]
