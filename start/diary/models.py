#encoding:utf-8
'''
日志相关数据结构
Created on Oct 8, 2015

@author: jh
'''
from django.db import models


class Diary(models.Model):
    class Meta:
        db_table = 'diary'
        index_together = [
            ["date", "type_code"],
        ]
        
    
    date = models.DateField(auto_now_add=True)
    type_code = models.CharField(max_length=32)
    title = models.CharField(max_length=64)
    content = models.TextField()
    user_id = models.IntegerField(blank=True,null=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
class DiaryType(models.Model):
    class Meta:
        db_table = 'diary_type'
    
    name = models.CharField(max_length=64)
    code = models.CharField(max_length=32)
    description = models.CharField(max_length=256,blank=True,null=True)
    user_id = models.IntegerField()
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)