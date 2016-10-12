# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('lepus', '0002_auto_20150913_1811'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='question',
            options={'ordering': ('category', 'ordering', 'id')},
        ),
        migrations.AlterField(
            model_name='answer',
            name='answer',
            field=models.CharField(max_length=256, verbose_name=b'\xe8\xa7\xa3\xe7\xad\x94'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'\xe4\xbd\x9c\xe6\x88\x90\xe6\x97\xa5\xe6\x99\x82'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(verbose_name=b'\xe5\x95\x8f\xe9\xa1\x8c', to='lepus.Question'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='team',
            field=models.ForeignKey(verbose_name=b'\xe3\x83\x81\xe3\x83\xbc\xe3\x83\xa0', to='lepus.Team'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name=b'\xe6\x9c\x80\xe7\xb5\x82\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xa5\xe6\x99\x82'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='user',
            field=models.ForeignKey(verbose_name=b'\xe3\x83\xa6\xe3\x83\xbc\xe3\x82\xb6\xe3\x83\xbc', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='attackpoint',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'\xe4\xbd\x9c\xe6\x88\x90\xe6\x97\xa5\xe6\x99\x82'),
        ),
        migrations.AlterField(
            model_name='attackpoint',
            name='point',
            field=models.IntegerField(verbose_name=b'\xe5\xbe\x97\xe7\x82\xb9'),
        ),
        migrations.AlterField(
            model_name='attackpoint',
            name='question',
            field=models.ForeignKey(verbose_name=b'\xe5\x95\x8f\xe9\xa1\x8c', to='lepus.Question'),
        ),
        migrations.AlterField(
            model_name='attackpoint',
            name='team',
            field=models.ForeignKey(verbose_name=b'\xe3\x83\x81\xe3\x83\xbc\xe3\x83\xa0', to='lepus.Team'),
        ),
        migrations.AlterField(
            model_name='attackpoint',
            name='token',
            field=models.CharField(unique=True, max_length=256, verbose_name=b'\xe3\x83\x88\xe3\x83\xbc\xe3\x82\xaf\xe3\x83\xb3'),
        ),
        migrations.AlterField(
            model_name='attackpoint',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name=b'\xe6\x9c\x80\xe7\xb5\x82\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xa5\xe6\x99\x82'),
        ),
        migrations.AlterField(
            model_name='attackpoint',
            name='user',
            field=models.ForeignKey(verbose_name=b'\xe3\x83\xa6\xe3\x83\xbc\xe3\x82\xb6\xe3\x83\xbc', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='category',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'\xe4\xbd\x9c\xe6\x88\x90\xe6\x97\xa5\xe6\x99\x82'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(unique=True, max_length=50, verbose_name=b'\xe3\x82\xab\xe3\x83\x86\xe3\x82\xb4\xe3\x83\xaa\xe5\x90\x8d'),
        ),
        migrations.AlterField(
            model_name='category',
            name='ordering',
            field=models.IntegerField(default=100, verbose_name=b'\xe8\xa1\xa8\xe7\xa4\xba\xe9\xa0\x86\xe5\xba\x8f'),
        ),
        migrations.AlterField(
            model_name='category',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name=b'\xe6\x9c\x80\xe7\xb5\x82\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xa5\xe6\x99\x82'),
        ),
        migrations.AlterField(
            model_name='config',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'\xe4\xbd\x9c\xe6\x88\x90\xe6\x97\xa5\xe6\x99\x82'),
        ),
        migrations.AlterField(
            model_name='config',
            name='key',
            field=models.CharField(unique=True, max_length=256, verbose_name=b'\xe8\xa8\xad\xe5\xae\x9a\xe9\xa0\x85\xe7\x9b\xae'),
        ),
        migrations.AlterField(
            model_name='config',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name=b'\xe6\x9c\x80\xe7\xb5\x82\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xa5\xe6\x99\x82'),
        ),
        migrations.AlterField(
            model_name='config',
            name='value_str',
            field=models.TextField(verbose_name=b'\xe3\x82\xb7\xe3\x83\xaa\xe3\x82\xa2\xe3\x83\xa9\xe3\x82\xa4\xe3\x82\xba\xe3\x81\x95\xe3\x82\x8c\xe3\x81\x9f\xe5\x80\xa4'),
        ),
        migrations.AlterField(
            model_name='file',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'\xe4\xbd\x9c\xe6\x88\x90\xe6\x97\xa5\xe6\x99\x82'),
        ),
        migrations.AlterField(
            model_name='file',
            name='file',
            field=models.FileField(upload_to=b'question/', max_length=256, verbose_name=b'\xe3\x83\x95\xe3\x82\xa1\xe3\x82\xa4\xe3\x83\xab'),
        ),
        migrations.AlterField(
            model_name='file',
            name='is_public',
            field=models.BooleanField(default=True, verbose_name=b'\xe5\x85\xac\xe9\x96\x8b\xe3\x81\x99\xe3\x82\x8b\xe3\x81\x8b'),
        ),
        migrations.AlterField(
            model_name='file',
            name='name',
            field=models.CharField(max_length=256, verbose_name=b'\xe3\x83\x95\xe3\x82\xa1\xe3\x82\xa4\xe3\x83\xab\xe5\x90\x8d'),
        ),
        migrations.AlterField(
            model_name='file',
            name='question',
            field=models.ForeignKey(verbose_name=b'\xe5\x95\x8f\xe9\xa1\x8c', to='lepus.Question'),
        ),
        migrations.AlterField(
            model_name='file',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name=b'\xe6\x9c\x80\xe7\xb5\x82\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xa5\xe6\x99\x82'),
        ),
        migrations.AlterField(
            model_name='flag',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'\xe4\xbd\x9c\xe6\x88\x90\xe6\x97\xa5\xe6\x99\x82'),
        ),
        migrations.AlterField(
            model_name='flag',
            name='point',
            field=models.IntegerField(verbose_name=b'\xe5\xbe\x97\xe7\x82\xb9'),
        ),
        migrations.AlterField(
            model_name='flag',
            name='question',
            field=models.ForeignKey(verbose_name=b'\xe5\x95\x8f\xe9\xa1\x8c', to='lepus.Question'),
        ),
        migrations.AlterField(
            model_name='flag',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name=b'\xe6\x9c\x80\xe7\xb5\x82\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xa5\xe6\x99\x82'),
        ),
        migrations.AlterField(
            model_name='notice',
            name='body',
            field=models.TextField(verbose_name=b'\xe6\x9c\xac\xe6\x96\x87'),
        ),
        migrations.AlterField(
            model_name='notice',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'\xe4\xbd\x9c\xe6\x88\x90\xe6\x97\xa5\xe6\x99\x82'),
        ),
        migrations.AlterField(
            model_name='notice',
            name='is_public',
            field=models.BooleanField(default=False, verbose_name=b'\xe5\x85\xac\xe9\x96\x8b\xe3\x81\xab\xe3\x81\x99\xe3\x82\x8b\xe3\x81\x8b'),
        ),
        migrations.AlterField(
            model_name='notice',
            name='title',
            field=models.CharField(max_length=80, verbose_name=b'\xe3\x82\xbf\xe3\x82\xa4\xe3\x83\x88\xe3\x83\xab'),
        ),
        migrations.AlterField(
            model_name='notice',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name=b'\xe6\x9c\x80\xe7\xb5\x82\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xa5\xe6\x99\x82'),
        ),
        migrations.AlterField(
            model_name='question',
            name='category',
            field=models.ForeignKey(verbose_name=b'\xe3\x82\xab\xe3\x83\x86\xe3\x82\xb4\xe3\x83\xaa', to='lepus.Category'),
        ),
        migrations.AlterField(
            model_name='question',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'\xe4\xbd\x9c\xe6\x88\x90\xe6\x97\xa5\xe6\x99\x82'),
        ),
        migrations.AlterField(
            model_name='question',
            name='is_public',
            field=models.BooleanField(default=False, verbose_name=b'\xe5\x85\xac\xe9\x96\x8b\xe3\x81\xab\xe3\x81\x99\xe3\x82\x8b\xe3\x81\x8b'),
        ),
        migrations.AlterField(
            model_name='question',
            name='max_answers',
            field=models.IntegerField(null=True, verbose_name=b'\xe6\x9c\x80\xe5\xa4\xa7\xe5\x9b\x9e\xe7\xad\x94\xe8\x80\x85\xe6\x95\xb0', blank=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='max_failure',
            field=models.IntegerField(null=True, verbose_name=b'\xe6\x9c\x80\xe5\xa4\xa7\xe5\x9b\x9e\xe7\xad\x94\xe6\x95\xb0', blank=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='ordering',
            field=models.IntegerField(default=100, verbose_name=b'\xe8\xa1\xa8\xe7\xa4\xba\xe9\xa0\x86\xe5\xba\x8f'),
        ),
        migrations.AlterField(
            model_name='question',
            name='sentence',
            field=models.TextField(verbose_name=b'\xe5\x95\x8f\xe9\xa1\x8c\xe6\x96\x87'),
        ),
        migrations.AlterField(
            model_name='question',
            name='title',
            field=models.CharField(max_length=50, verbose_name=b'\xe3\x82\xbf\xe3\x82\xa4\xe3\x83\x88\xe3\x83\xab'),
        ),
        migrations.AlterField(
            model_name='question',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name=b'\xe6\x9c\x80\xe7\xb5\x82\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xa5\xe6\x99\x82'),
        ),
        migrations.AlterField(
            model_name='team',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'\xe4\xbd\x9c\xe6\x88\x90\xe6\x97\xa5\xe6\x99\x82'),
        ),
        migrations.AlterField(
            model_name='team',
            name='last_score_time',
            field=models.DateTimeField(null=True, verbose_name=b'\xe6\x9c\x80\xe7\xb5\x82\xe5\xbe\x97\xe7\x82\xb9\xe6\x97\xa5\xe6\x99\x82', blank=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='name',
            field=models.CharField(unique=True, max_length=32, verbose_name=b'\xe3\x83\x81\xe3\x83\xbc\xe3\x83\xa0\xe5\x90\x8d'),
        ),
        migrations.AlterField(
            model_name='team',
            name='password',
            field=models.CharField(max_length=128, verbose_name=b'\xe3\x83\x81\xe3\x83\xbc\xe3\x83\xa0\xe3\x83\x91\xe3\x82\xb9\xe3\x83\xaf\xe3\x83\xbc\xe3\x83\x89'),
        ),
        migrations.AlterField(
            model_name='team',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name=b'\xe6\x9c\x80\xe7\xb5\x82\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xa5\xe6\x99\x82'),
        ),
        migrations.AlterField(
            model_name='user',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'\xe4\xbd\x9c\xe6\x88\x90\xe6\x97\xa5\xe6\x99\x82'),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_score_time',
            field=models.DateTimeField(null=True, verbose_name=b'\xe6\x9c\x80\xe7\xb5\x82\xe5\xbe\x97\xe7\x82\xb9\xe6\x97\xa5\xe6\x99\x82', blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='seat',
            field=models.CharField(max_length=32, verbose_name=b'\xe5\xba\xa7\xe5\xb8\xad', blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='team',
            field=models.ForeignKey(verbose_name=b'\xe3\x83\x81\xe3\x83\xbc\xe3\x83\xa0', blank=True, to='lepus.Team', null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name=b'\xe6\x9c\x80\xe7\xb5\x82\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xa5\xe6\x99\x82'),
        ),
        migrations.AlterField(
            model_name='userconnection',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'\xe4\xbd\x9c\xe6\x88\x90\xe6\x97\xa5\xe6\x99\x82'),
        ),
        migrations.AlterField(
            model_name='userconnection',
            name='ip',
            field=models.GenericIPAddressField(verbose_name=b'IP\xe3\x82\xa2\xe3\x83\x89\xe3\x83\xac\xe3\x82\xb9'),
        ),
        migrations.AlterField(
            model_name='userconnection',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name=b'\xe6\x9c\x80\xe7\xb5\x82\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xa5\xe6\x99\x82'),
        ),
        migrations.AlterField(
            model_name='userconnection',
            name='user',
            field=models.ForeignKey(verbose_name=b'\xe3\x83\xa6\xe3\x83\xbc\xe3\x82\xb6\xe3\x83\xbc', to=settings.AUTH_USER_MODEL),
        ),
    ]
