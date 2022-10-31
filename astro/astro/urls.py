from django.contrib import admin
from django.urls import path, include
from home.views import HomePage

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", HomePage.as_view(), name="home"),
    path("polls/", include("polls.urls")),
]
