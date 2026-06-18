import time
from django.http import HttpResponseForbidden
class LogRequestMiddelware:
    def __init__(self,get_response):
        self.get_response=get_response
    
    def __call__(self, request):
        # process before view
        print(f'Middleware Request path:{request.path}')
        response=self.get_response(request)
        #process after view
        print(f'Middleware response status: {response.status_code}')
        return response 
        


class TimerMiddleware:
    def __init__(self,get_response):
        self.get_response=get_response
    
    def __call__(self, request):
        # process before view
        start= time.time()
        print(f'time taken for request:{start}')
        response=self.get_response(request)
        duration =time.time()-start
        #process after view
        print(f'time taken for response: {duration:.3f} seconds')
        return response 
    

class BlockIp:
    BlockedIps=["127.0.0.1"]
    def __init__(self,get_response):
        self.get_response=get_response
    
    def __call__(self, request):
        ip=request.META.get("REMOTE_ADDR")
        if ip in self.BlockedIps:
            return HttpResponseForbidden("Your Ip is blocked")
        response=self.get_response(request)
        return response
            