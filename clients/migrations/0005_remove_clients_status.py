# Generated by Django 4.2 on 2023-05-02 19:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0004_alter_clients_age_alter_clients_phone_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clients',
            name='status',
        ),
    ]
