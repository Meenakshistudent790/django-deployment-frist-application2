from django.shortcuts import render
from django.http import HttpResponse;

# Create your views here.
def f1(request):
    return HttpResponse("<h2>Good Morning user...!! Have a nice day..</h2><hr/>");
def f2(request):
    return Httpresponse("<h2>Good afternoon user...!! hope you are doing good..</h2><hr/>");
def f3(request):
    return HttpResponse("<h2>Good Evening user..!! how war ur day...</h2></hr>");
