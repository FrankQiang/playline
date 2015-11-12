# -*- coding:utf-8 -*-
from django import forms
 
class LifeForm(forms.Form):
    TIME = 'time'
    ABILITY = 'ability'
    IDLE = 'idle'
    LIFE_TYPE_CHOICES = ((TIME, '时间交易'),(ABILITY, '能力交换'),(IDLE, '闲物交换'),)

    title = forms.CharField(label='标题',widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'标题'}))
    life_type_choices = forms.ChoiceField(label='',choices=LIFE_TYPE_CHOICES)
    info = forms.CharField(label='简介',widget=forms.Textarea(attrs={'cols': 75, 'rows': 10,'class': 'form-control','placeholder':'请介绍你的交易单内容'}))
    
