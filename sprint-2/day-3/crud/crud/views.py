from django.http import HttpResponse;
from django.shortcuts import render;
import store;

def index(request):
   list = store.getUser()
   return render(request,'index.html',{"users":list})

def read(request):
    return HttpResponse('<h1>Welcome!! Sumat </h1>')

def write(request):
    return HttpResponse('<h1>Welcome!! Sumat </h1>')


def update(request):
    return HttpResponse('<h1>Welcome!! Sumat </h1>')

def delete(request):
    return HttpResponse('<h1>Welcome!! Sumat </h1>')