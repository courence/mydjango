#!/usr/bin/python
# encoding:utf-8
'''

Created on Oct 9, 2015

@author: jh
'''
from django.conf.urls import url

from diary.views.diaryView import DiaryView


urlpatterns = [
    url(r'^index/$', DiaryView.base,{'action':'index'},name="index"),
    url(r'^add/$', DiaryView.base,{'action':'add'},name="add"),
]