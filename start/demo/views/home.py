#!/usr/bin/python
# encoding:utf-8
'''

Created on Oct 9, 2015

@author: jh
'''

from datetime import datetime

from common.base_views import BaseViews


class HomeViews(BaseViews):

    @classmethod
    def base(cls, request, *args, **kwargs):
        return super(HomeViews, cls).base(request, *args, **kwargs)
    
    def test(self,*args,**kwargs):
        now = datetime.now()
        return self.render('demo/home/test.html',{"now":now})