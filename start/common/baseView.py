#!/usr/bin/python
# encoding:utf-8
'''

Created on Oct 9, 2015

@author: jh
'''

from django.core.urlresolvers import reverse
from django.http import Http404
from django.shortcuts import render, HttpResponseRedirect


class BaseView(object):

    @classmethod
    def base(cls, request, *args, **kwargs):

        if "action" not in kwargs:
            raise Http404(u"缺少action，请检查 url")

        if "method" in kwargs and request.method != kwargs["method"].upper():
            raise Http404(u"http请求方法错误")
        
        action = kwargs['action']
        
        if not hasattr(cls, action):
            raise Http404(u"找不到路由中指定的action:%s"%action)
        
        self = cls()

        '''定义实例变量'''
        self.request = request
        self.action = action
        self.args = args
        self.kwargs = kwargs

        '''根据http 方法来定义 PARAMS'''
        if request.method in ("POST", "PUT"):
            self.params = request.POST
        elif  request.method in ("GET"):
            self.params = request.GET
        else:
            raise Http404(u"未处理的http传输方式:%s"%request.method)

        '''执行相应action的实例方法'''
        
        return getattr(self, action)(request)
            
            
    def render(self, template, context={} ,**kwargs):
        
        return render(self.request,template,context)
    
    def redirect(self,viewname, *args, **kwargs):
        '''重定向'''
        return HttpResponseRedirect(reverse(viewname))
        