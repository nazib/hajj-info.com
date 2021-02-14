from django.shortcuts import render

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

'''
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

'''
def homepage(request):
    return render(request,"home.html",{})

def howto(request):
    return render(request,"howto.html",{})

def history(request):
    return render(request,"history.html",{})

def QandH(request):
    return render(request,"Q&H.html",{})

def visa(request):
    return render(request,"visa.html",{})

def agents(request):
    return render(request,"agents.html",{})

def hotels(request):
    return render(request,"hotels.html",{})

def rentals(request):
    return render(request,"rentals.html",{})

def flights(request):
    return render(request,"flights.html",{})

def blog(request):
    return render(request,"blog.html",{})

