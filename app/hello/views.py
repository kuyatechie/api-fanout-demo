from django.shortcuts import render
from django.http import HttpResponse
from constance import config

def index(request):
    return HttpResponse(config.MESSAGE)