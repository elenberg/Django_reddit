# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_submitted', models.DateTimeField(auto_now_add=True)),
                ('rank', models.FloatField(default=0.0)),
                ('description', models.TextField(verbose_name=b'Description', blank=True)),
                ('comments', models.ForeignKey(related_name='replies', blank=True, to='threads.Comment', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.TextField(max_length=100, verbose_name=b'Headline')),
                ('internal', models.TextField(max_length=100, verbose_name=b'Internal Link')),
                ('date_submitted', models.DateTimeField(auto_now_add=True)),
                ('rank', models.FloatField(default=0.0)),
                ('url', models.URLField(max_length=100, verbose_name=b'URL', blank=True)),
                ('description', models.TextField(verbose_name=b'Description', blank=True)),
                ('submitter', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Subreddit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.TextField(max_length=30)),
                ('slug', models.TextField(max_length=30, null=True)),
                ('creator', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comment', models.ForeignKey(related_name='vote', blank=True, to='threads.Comment', null=True)),
                ('link', models.ForeignKey(related_name='vote', blank=True, to='threads.Link', null=True)),
                ('voter', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='link',
            name='subreddit',
            field=models.ForeignKey(related_name='links', to='threads.Subreddit', null=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='link',
            field=models.ForeignKey(related_name='replies', blank=True, to='threads.Link', null=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='submitter',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
