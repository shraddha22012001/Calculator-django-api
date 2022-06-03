from django.shortcuts import render
from django.http import HttpResponse
from django.core.serializers import serialize
import json
import random           

def home(request):
    return render(request,"home.html")
def index(request):
    return render(request,"index.html")
def result(request):
    fnum=int(request.GET['fnum'])
    snum=int(request.GET['snum'])
    opt=request.GET['oper']
    if(opt=="1"):
       Operator="Addition"
       userans=fnum+snum
    elif(opt=="2"):
       Operator="Subtraction"
       userans=fnum-snum
    elif(opt=="3"):
       Operator="Multiplication"
       userans=fnum*snum
    elif(opt=="4"):
       Operator="Division"
       userans=fnum/snum
    else:
       Operator="Invalid"
       userans="Please Select Valid Operator"
    resultdict={'answer':userans,'fnum':fnum,'snum':snum,'operator':Operator}
    response=json.dumps(resultdict,indent=5)
    return HttpResponse(response,content_type='application/json')