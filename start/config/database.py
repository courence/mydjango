#encoding:utf-8
'''
数据库配置
Created on Sep 20, 2015

@author: jh
'''
import os
from settings import ROOT
DATABASES = {
    'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'wait_and_hope',
#         'USER':'root',
#         'PASSWORD':'root',
#         'HOST':'127.0.0.1'
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(ROOT,'start.db'),
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
             
}