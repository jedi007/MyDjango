from django.shortcuts import render

from django.http import HttpResponse

import json

from django.views.decorators.csrf import csrf_exempt


from .fLogger import logger

from .myModels.computerplayer import computerplayter


def index(request):
    return render(request,'gobang/index.html')

#客户端提交的post如果不加下面这行，会出现403error
@csrf_exempt
def py_step(request):
    if request.method == "POST":
        logger.info("get post method")
        name = request.POST.get('name')
        steps = request.POST.get('steps')
        checkerboard = request.POST.get('checkerboard')

        beststep = computerplayter.computestep(steps,checkerboard) 
        logger.info("beststep:"+json.dumps(beststep))

        return HttpResponse(json.dumps(beststep))
    else:
        return HttpResponse(json.dumps({
            "name": "returnname-",
            "status": "1",
            "result": "failed"
        }))


# Create your views here.
