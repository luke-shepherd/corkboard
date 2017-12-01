# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-01 00:35
from __future__ import unicode_literals

import comapi.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('comapi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BoardUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=1000)),
            ],
        ),
        migrations.AddField(
            model_name='boardpost',
            name='post_creator',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='board',
            name='creator',
            field=models.ForeignKey(on_delete=models.SET(comapi.models.get_sentinel_user), to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='boarduser',
            name='legacy_boards',
            field=models.ManyToManyField(to='comapi.Board'),
        ),
        migrations.AddField(
            model_name='boarduser',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
