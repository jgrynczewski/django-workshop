# Generated by Django 5.1.4 on 2024-12-11 01:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms_and_views_app', '0002_ticket'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='registered',
            field=models.DateTimeField(default=datetime.datetime(2024, 12, 11, 1, 18, 52, 680309, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
    ]
