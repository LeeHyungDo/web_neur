#import sys
#import time
#import json

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

#from django.conf import settings
#from flask.wrappers import Response

fresh =False

class RefreshEventHandler(FileSystemEventHandler):
    def on_created(self, event):
        global fresh
        fresh = True
        print 'startTo~'
        
        
class watchdogMiddleware(object):
    def process_response(self, request, response):
        global fresh
        
        print 'getstart'
        '''try: 
            mimetype = response._header['content-type'][1]
        except KeyError:
            return response
          
        if mimetype == 'application/json':
            items = json.loads(response.content)
            if fresh and items.get('fresh') is not None:
                fresh = False
                items['fresh']=True
                response.content = json.dumps(items)''' 
        
        
        return response
    def wather(self):
        observer =Observer()
        
        path = '/media/animation'
        event_handler = RefreshEventHandler()
        observer.schedule(event_handler, path, recursive=False)
        
        observer.start()
        
    __REGISTERED_=False
    
    def __init__(self):
        if watchdogMiddleware.__REGISTERED_:
            return
        self.wather()
        watchdogMiddleware.__REGISTERED_ = True


