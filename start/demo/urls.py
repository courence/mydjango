#!/usr/bin/python
# encoding:utf-8
'''

Created on Oct 9, 2015

@author: jh
'''
from django.conf.urls import url

from demo.views.home import HomeViews


urlpatterns = [
    url(r'^home/test/$', HomeViews.base,{'action':'test'},name="home_test"),
]