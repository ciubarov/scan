# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-03 21:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20160804_0004'),
    ]

    operations = [
        migrations.AddField(
            model_name='promotion',
            name='friends',
            field=models.ManyToManyField(related_name='_promotion_friends_+', to='app.Promotion'),
        ),
    ]
