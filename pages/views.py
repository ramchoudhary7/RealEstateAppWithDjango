from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('<H1>SUCCESS</H1>')

# Create your views here.
