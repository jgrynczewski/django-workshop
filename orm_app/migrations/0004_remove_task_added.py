# Generated by Django 5.1.4 on 2024-12-10 11:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orm_app', '0003_task_added'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='added',
        ),
    ]
