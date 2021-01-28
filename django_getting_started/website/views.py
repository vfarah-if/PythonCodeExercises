from datetime import datetime

from django.http import HttpResponse


def welcome(request):
    return HttpResponse("Welcome to the meeting planner! " + str(datetime.utcnow()))


def about(request):
    return HttpResponse("My name is Vincent Farah and I am new to Python and Django")
