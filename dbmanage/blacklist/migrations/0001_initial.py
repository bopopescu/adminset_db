# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-14 03:34
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tb_blacklist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dbtag', models.CharField(max_length=255, unique=True)),
                ('tbname', models.TextField(max_length=255)),
                ('user_permit', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'tb_blacklist',
            },
        ),
    ]
