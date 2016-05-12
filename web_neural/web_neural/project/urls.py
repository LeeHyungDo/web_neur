# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

urlpatterns = patterns('web_neural.project.views',
        url(r'^list/$', 'list', name='list'),
        url(r'^conversing/$', 'conversing', name='conversing'),
        url(r'^imge/$', 'imge', name='imge'),
        url(r'^stylelist/$', 'stylelist', name='stylelist'),
)
