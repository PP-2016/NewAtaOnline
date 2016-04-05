# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Avaliation',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Notebook',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('date', models.DateField(auto_now=True)),
                ('content', models.CharField(max_length=150)),
                ('grade', models.ForeignKey(to='Ata.Avaliation')),
            ],
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('number_id', models.IntegerField()),
                ('email', models.EmailField(max_length=200)),
                ('name', models.CharField(max_length=50)),
                ('admin', models.BooleanField()),
                ('formation', models.CharField(max_length=200)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('number_id', models.IntegerField()),
                ('email', models.EmailField(max_length=200)),
                ('name', models.CharField(max_length=50)),
                ('admin', models.BooleanField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='avaliation',
            name='record',
            field=models.ForeignKey(to='Ata.Notebook'),
        ),
    ]
