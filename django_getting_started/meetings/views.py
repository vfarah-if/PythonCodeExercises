from django.shortcuts import render, get_object_or_404

from meetings.models import Meeting, Room


def detail(request, meeting_id):
    # meeting = Meeting.objects.get(pk=meeting_id)
    meeting = get_object_or_404(Meeting, pk=meeting_id)
    data = dict(meeting=meeting)
    return render(request, "meetings/detail.html", data)


def rooms(request):
    all_rooms = Room.objects.all()
    data = dict(rooms=all_rooms)
    return render(request, "meetings/rooms.html", data)
