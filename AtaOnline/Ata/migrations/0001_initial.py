# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Avaliation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
            ],
        ),
        migrations.CreateModel(
            name='Notebook',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=50)),
                ('date', models.DateField(auto_now=True)),
                ('content', models.CharField(max_length=250)),
                ('grade', models.ForeignKey(to='Ata.Avaliation')),
            ],
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('number_id', models.IntegerField()),
                ('formation', models.CharField(max_length=200)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('number_id', models.IntegerField()),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='avaliation',
            name='record',
            field=models.ForeignKey(to='Ata.Notebook'),
        ),
    ]
