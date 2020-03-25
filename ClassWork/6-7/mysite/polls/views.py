from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def indext(request):
    return HttpResponse('Hello Word..!')