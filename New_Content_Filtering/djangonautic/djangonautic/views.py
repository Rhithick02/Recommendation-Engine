from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    return HttpResponse('WELCOME TO HOMEPAGE!!! MovieRecommendation engine')

def about(request):
    return HttpResponse('WELCOME TO ABOUT PAGE.')