from django.http import HttpResponse
from django.shortcuts import render


def home(request):
   # return HttpResponse("Welcome to the !")
   return render(request, "website/superman.html")


def card(request):
    return HttpResponse("Patte na khel ladle")

