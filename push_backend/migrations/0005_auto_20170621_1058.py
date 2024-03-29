# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-21 08:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('push_backend', '0004_auto_20170608_0056'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('what', models.CharField(max_length=200)),
                ('when', models.CharField(max_length=200)),
                ('offer', models.CharField(max_length=200)),
                ('picture', models.ImageField(blank=True, upload_to='', verbose_name='photos/')),
                ('created_on', models.TimeField(auto_now=True)),
            ],
        ),
        migrations.AlterField(
            model_name='image',
            name='description',
            field=models.CharField(default='No Description', max_length=350),
        ),
        migrations.AlterField(
            model_name='image',
            name='file',
            field=models.ImageField(blank=True, upload_to='photos/'),
        ),
    ]
