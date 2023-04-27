from django.shortcuts import render

# Create your views here.

def hello(request):
    d={'name':'seshulu','age':22}
    return render(request,'hello.html',d)