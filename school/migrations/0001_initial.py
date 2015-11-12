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
            name='Life',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pub_date', models.DateTimeField()),
                ('title', models.CharField(max_length=90)),
                ('info', models.TextField(max_length=300)),
                ('life_type_choices', models.CharField(default=b'time', max_length=7, choices=[(b'time', b'\xe6\x97\xb6\xe9\x97\xb4\xe4\xba\xa4\xe6\x98\x93'), (b'ability', b'\xe8\x83\xbd\xe5\x8a\x9b\xe4\xba\xa4\xe6\x8d\xa2'), (b'idle', b'\xe9\x97\xb2\xe7\x89\xa9\xe4\xba\xa4\xe6\x8d\xa2')])),
                ('watch', models.IntegerField(default=0)),
                ('like', models.IntegerField(default=0)),
                ('image', models.CharField(max_length=256)),
                ('expired', models.BooleanField(default=False)),
                ('accept', models.BooleanField(default=False)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
