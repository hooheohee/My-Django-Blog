# Generated by Django 2.2.1 on 2019-05-06 22:55

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 6, 22, 55, 11, 218376, tzinfo=utc)),
        ),
    ]
