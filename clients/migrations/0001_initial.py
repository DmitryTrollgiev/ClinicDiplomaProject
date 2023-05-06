# Generated by Django 4.2 on 2023-05-01 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10000, null=True, verbose_name='Имя')),
                ('sex', models.TextField(null=True, verbose_name='Пол')),
                ('polis', models.TextField(null=True, verbose_name='ПОЛИС ОМС')),
                ('passport_number', models.TextField(null=True, verbose_name='Серия и номер паспорта')),
                ('phone', models.TextField(null=True, verbose_name='Телефон')),
                ('age', models.TextField(null=True, verbose_name='Возраст')),
            ],
            options={
                'verbose_name': 'Клиент',
                'verbose_name_plural': 'Клиенты',
                'db_table': 'clients',
            },
        ),
    ]
