from django.http import HttpResponse
from django.shortcuts import render


def welcome(request):
    data = dict(message="Test to see the rendered using the template structure")
    return render(request, 'website/welcome.html', data)


def about(request):
    return HttpResponse("My name is Vincent Farah and I am new to Python and Django")
