# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-07 20:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0002_auto_20170907_2019'),
        ('article', '0003_article_cat'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='newsletter',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='newsletter.Newsletter'),
        ),
    ]