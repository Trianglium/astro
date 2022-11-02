from django.urls import path
from .views import PollsIndex, PollDetail

app_name = "polls"
urlpatterns = [
    path("", PollsIndex.as_view(), name="polls-index"),
    path("<int:question_id>/", PollDetail.as_view(), name="poll-detail"),
]
