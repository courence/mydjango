#encoding:utf-8
'''
日志相关
Created on Feb 24, 2016
@author: jh
'''


from datetime import datetime
from django.core.urlresolvers import reverse

from common.baseview import BaseView
from diary.models import Diary


class DiaryView(BaseView):

    @classmethod
    def base(cls, request, *args, **kwargs):
        return super(DiaryView, cls).base(request, *args, **kwargs)
    
    def index(self,*args,**kwargs):
        diarys = Diary.objects.all()[0:10]
        return self.render('diary/index.html',{"diarys":diarys})
    
    def add(self,*args,**kwargs):
        now = datetime.now()
        today = now.strftime("%Y-%m-%d")
        if self.request.method == "POST":
            title = self.request.POST.get('title',today)
            content = self.request.POST.get('content')
            if title and content:
                diary = Diary()
                diary.title = title
                diary.content = content
                diary.save()
                return self.redirect('diary:index')
        return self.render('diary/add.html',{'today':today})