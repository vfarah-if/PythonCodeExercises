from django.shortcuts import render, get_object_or_404, redirect
# from django.forms import modelform_factory
from meetings.forms import MeetingForm
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

# REMARKS: This is the original way with
# MeetingForm = modelform_factory(Meeting, exclude=[])


def create(request):
    if request.method == "POST":
        form = MeetingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = MeetingForm()

    data = dict(form=form)
    return render(request, "meetings/create.html", data)
