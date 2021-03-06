# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-11 02:39
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('exchange', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Participants',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='exchange',
            name='name',
            field=models.CharField(default='default name', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='exchange',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='participants',
            name='exchange',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='participants', to='exchange.Exchange'),
        ),
        migrations.AddField(
            model_name='participants',
            name='participant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
