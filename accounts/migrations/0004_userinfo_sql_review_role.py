# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-26 13:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sql', '0001_initial'),
        ('accounts', '0003_auto_20171124_1105'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='sql_review_role',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='sql.sqlreview_role'),
        ),
    ]
