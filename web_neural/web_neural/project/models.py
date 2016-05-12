# -*- conding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Subject(models.Model):
    subjectfile = models.ImageField(upload_to='subject/%Y%m%d')

class Style(models.Model):
    stylefile = models.ImageField(upload_to='style/%Y%m%d')

class Conversegpu(models.Model):
    congpufile = models.TextField(max_length=500)
        
    def get_file_name(self):
        return self.congpufile

class Conversecpu(models.Model):
    concpufile = models.TextField(max_length=500)
        
    def get_file_name(self):
        return self.concpufile    
    
