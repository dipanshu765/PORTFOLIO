# Generated by Django 3.1.2 on 2020-10-18 09:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_auto_20201018_1421'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 18, 14, 46, 36, 703445)),
        ),
    ]
