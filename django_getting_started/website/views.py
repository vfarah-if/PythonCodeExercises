from django.http import HttpResponse
from django.shortcuts import render

from meetings.models import Meeting, Room


def welcome(request):
    data = dict(
        message="Test to see the rendered using the template structure",
        meetings_count=Meeting.objects.count(),
        meetings=Meeting.objects.all(),
        rooms_count=Room.objects.count()
    )
    return render(request, 'website/welcome.html', data)


def about(request):
    return HttpResponse("My name is Vincent Farah and I am new to Python and Django")
