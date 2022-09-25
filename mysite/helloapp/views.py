from django.shortcuts import render
from django.http import HttpResponse
def hello(request):
    return HttpResponse("Hello World!I am coming...")
# Create your views here.
