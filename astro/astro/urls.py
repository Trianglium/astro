from django.contrib import admin
from django.conf import settings

from django.urls import path, include
from home.views import HomePage, AboutPage

urlpatterns = [
    # path("admin/", admin.site.urls),
    path("", HomePage.as_view(), name="home"),
    path("about/", AboutPage.as_view(), name="about"),
    path("polls/", include("polls.urls")),
    path("learn/", include("faq.urls")),
    path("forum/", include("forum.urls")),
]
