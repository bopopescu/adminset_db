# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-14 03:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Passwd_forget',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('vc_value', models.CharField(db_index=True, max_length=40)),
                ('is_valid', models.SmallIntegerField(default=1)),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.AlterIndexTogether(
            name='passwd_forget',
            index_together=set([('username', 'is_valid')]),
        ),
    ]
