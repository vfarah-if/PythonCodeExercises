from django.urls import path

from meetings.views import detail, rooms, create

urlpatterns = [
    path('<int:meeting_id>', detail, name="detail"),
    path('rooms', rooms, name="rooms"),
    path('create', create, name="create")
]
