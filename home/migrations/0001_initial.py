# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-09 02:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('addressL1', models.CharField(max_length=254)),
                ('addressL2', models.CharField(max_length=254)),
                ('city', models.CharField(max_length=254)),
                ('province', models.CharField(max_length=254)),
                ('postal', models.CharField(max_length=254)),
                ('additionalInfo', models.CharField(max_length=254)),
                ('sub_mgr_acct_id_label', models.CharField(max_length=254)),
            ],
        ),
    ]