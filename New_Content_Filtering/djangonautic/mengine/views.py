from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def homepage(request):
    return HttpResponse('You are at homepage of movie RE')

def searchbar(request):
    # return HttpResponse('Hi')
    return render(request, 'searchbar.html')

def imagepage(request):
    return render(request, 'imagepage.html')