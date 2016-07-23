import sys
#sys.path.append("/root/CLevelSegmentDemo/ACL2013-CharParsing/ZPar-RunExample")
from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
#from segmentjson import SegJson

def hello_world(request):
    return render(request, 'hello_world.html', {
        'current_time': datetime.now(),
    })

def demo(request,stn):
    if stn:
        prediction=SegJson(stn.encode('utf-8')) 
    return render(request, 'demo.html', {
        'stn':stn,
        'prediction':prediction,
    })
