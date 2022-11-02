from django.urls import path
from .views import PollsIndex, PollDetail, PollResults, vote

app_name = "polls"
urlpatterns = [
    path("", PollsIndex.as_view(), name="polls-index"),
    path("<int:pk>/", PollDetail.as_view(), name="poll-detail"),
    path("<int:pk>/results/", PollResults.as_view(), name="poll-results"),
    path("<int:question_id>/vote/", vote, name="poll-vote"),
]
