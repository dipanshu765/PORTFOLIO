# Generated by Django 3.1.2 on 2020-10-17 14:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='mobile',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='contact',
            name='timing',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 17, 20, 8, 58, 801587)),
        ),
    ]
