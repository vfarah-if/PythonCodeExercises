from django.http import HttpResponse
from django.shortcuts import render


def welcome(request):
    return render(request, 'website/welcome.html')


def about(request):
    return HttpResponse("My name is Vincent Farah and I am new to Python and Django")
