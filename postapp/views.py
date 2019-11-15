from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request,'input.html')
def add(request):
    try:
        v1=request.POST["t1"]
        v2=request.POST["t2"]
        i=int(v1)
        j=int(v2)
        k=i+j
        return HttpResponse("sum is:"+str(k))
    except:
        return render(request,'input.html')