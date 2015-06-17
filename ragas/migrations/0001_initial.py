# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('artist_name', models.CharField(max_length=200)),
                ('gharana', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Bandish',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('bandish_title', models.CharField(max_length=200)),
                ('original_composer', models.ForeignKey(to='ragas.Artist')),
            ],
        ),
        migrations.CreateModel(
            name='FilmSong',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('song_name', models.CharField(max_length=200)),
                ('film', models.CharField(max_length=200)),
                ('pub_date', models.DateField(verbose_name=b'date published')),
            ],
        ),
        migrations.CreateModel(
            name='Raga',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('raga_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Recording',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pub_date', models.DateField(verbose_name=b'date published')),
                ('artist', models.ForeignKey(to='ragas.Artist')),
            ],
        ),
        migrations.CreateModel(
            name='Thaat',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('thaat_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='raga',
            name='tht',
            field=models.ForeignKey(to='ragas.Thaat'),
        ),
        migrations.AddField(
            model_name='filmsong',
            name='rg',
            field=models.ForeignKey(to='ragas.Raga'),
        ),
        migrations.AddField(
            model_name='bandish',
            name='rg',
            field=models.ForeignKey(to='ragas.Raga'),
        ),
    ]
