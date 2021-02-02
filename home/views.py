from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

'''
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

'''
def homepage(request):
    #template = loader.get_template("rankapp/page.html")
    return render(request,"page.html",{})