from django.shortcuts import render

from meetings.models import Meeting


def detail(request, meeting_id):
    meeting = Meeting.objects.get(pk=meeting_id)
    data = dict(meeting=meeting)
    return render(request, "meetings/detail.html", data)
