# Generated by Django 5.1.4 on 2024-12-10 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orm_app', '0002_rename_name_task_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='added',
            field=models.DateTimeField(auto_now_add=True, default=None),
            preserve_default=False,
        ),
    ]
