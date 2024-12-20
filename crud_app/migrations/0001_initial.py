# Generated by Django 5.1.4 on 2024-12-11 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=256)),
                ('category', models.IntegerField(choices=[(1, 'Comedy'), (2, 'Thriller'), (3, 'Romance')])),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
    ]
