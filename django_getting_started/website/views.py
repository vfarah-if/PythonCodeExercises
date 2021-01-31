from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime

from meetings.models import Meeting, Room


def welcome(request):
    data = dict(
        message="Test to see the rendered using the template structure",
        meetings_count=Meeting.objects.count(),
        meetings=Meeting.objects.filter(date__gte=datetime.now()).order_by('date'),
        archived_meetings=Meeting.objects.filter(date__lt=datetime.now()).order_by('-date'),
        rooms_count=Room.objects.count()
    )
    return render(request, 'website/welcome.html', data)


def about(request):
    return HttpResponse("My name is Vincent Farah and I am new to Python and Django")
