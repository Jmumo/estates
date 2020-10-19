# Generated by Django 3.1.2 on 2020-10-19 05:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('listing', models.CharField(max_length=200)),
                ('listing_id', models.ImageField(upload_to='')),
                ('name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('message', models.TextField(blank=True)),
                ('contact', models.DateTimeField(blank=True, default=datetime.datetime(2020, 10, 19, 8, 5, 59, 756993))),
                ('user_id', models.IntegerField(blank=True)),
            ],
        ),
    ]
