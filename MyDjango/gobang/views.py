from django.shortcuts import render

from django.http import HttpResponse

import json

from django.views.decorators.csrf import csrf_exempt


from .fLogger import logger


def index(request):
    return render(request,'gobang/index.html')

#客户端提交的post如果不加下面这行，会出现403error
@csrf_exempt
def py_step(request):
    if request.method == "POST":
        logger.info("test post")
        name = request.POST.get('name')
        checkerboard = request.POST.get('checkerboard')
        logger.info(type(checkerboard))
        logger.info("checkerboard:"+str(checkerboard))
        return HttpResponse(json.dumps({
            "name": "returnname-"+name,
            "status": "1",
            "result": "ok"
        }))
    else:
        return HttpResponse(json.dumps({
            "name": "returnname-",
            "status": "1",
            "result": "failed"
        }))


# Create your views here.
