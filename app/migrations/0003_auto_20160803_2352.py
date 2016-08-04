# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-03 20:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_article_logo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(default='/uploads/None/no-img.jpg', upload_to='/uploads/')),
                ('phone', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=200)),
                ('website', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Promotion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('background', models.ImageField(default='/uploads/None/no-img.jpg', upload_to='/uploads/')),
                ('image', models.ImageField(default='/uploads/None/no-img.jpg', upload_to='/uploads/')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('help_text', models.CharField(max_length=200)),
                ('post_text', models.TextField()),
                ('year_in_school', models.CharField(choices=[('FR', 'Freshman'), ('SO', 'Sophomore'), ('JR', 'Junior'), ('SR', 'Senior')], default='FR', max_length=2)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Company')),
            ],
        ),
        migrations.RemoveField(
            model_name='article',
            name='user',
        ),
        migrations.DeleteModel(
            name='Article',
        ),
    ]
