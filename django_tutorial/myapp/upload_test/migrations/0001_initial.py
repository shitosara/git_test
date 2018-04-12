# Generated by Django 2.0.3 on 2018-03-18 16:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FileName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.CharField(max_length=50, verbose_name='ファイル名')),
                ('upload_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='アップロード日時')),
            ],
        ),
    ]
