# -*- coding:utf-8 -*-
from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User


class Life(models.Model):
    user = models.ForeignKey(User)
    TIME = 'time'
    ABILITY = 'ability'
    IDLE = 'idle'
    LIFE_TYPE_CHOICES = ((TIME, '时间交易'),(ABILITY, '能力交换'),(IDLE, '闲物交换'),)
    pub_date = models.DateTimeField()
    title = models.CharField(max_length=90)
    info = models.TextField(max_length=300)
    life_type_choices = models.CharField(max_length=7,choices=LIFE_TYPE_CHOICES,default=TIME)
    watch = models.IntegerField(default=0)
    like = models.IntegerField(default=0)
    image = models.CharField(max_length=256)
    expired = models.BooleanField(default=False)
    accept = models.BooleanField(default=False)
    accept_id = models.IntegerField(default=0)
    

    def __unicode__(self):
        return u'%s' % (self.title)
    
    
