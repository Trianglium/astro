from django.urls import path
from .views import PollsIndex, PollDetail

app_name = "polls"
urlpatterns = [
    path("", PollsIndex.as_view(), name="polls-index"),
    path("<int:id>/", PollDetail.as_view(), name="poll-detail"),
]
