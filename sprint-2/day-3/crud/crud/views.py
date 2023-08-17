from django.http import HttpResponse;
from django.shortcuts import render;


def index(request):
   return render(request,'index.html')

def read(request):
    return HttpResponse('<h1>Welcome!! Sumat </h1>')

def write(request):
    return HttpResponse('<h1>Welcome!! Sumat </h1>')


def update(request):
    return HttpResponse('<h1>Welcome!! Sumat </h1>')

def delete(request):
    return HttpResponse('<h1>Welcome!! Sumat </h1>')