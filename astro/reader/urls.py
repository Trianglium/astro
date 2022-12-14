from django.urls import path
from .views import DocIndex, DocDetail

app_name = "reader"
urlpatterns = [
    path("", DocIndex.as_view(), name="doc-index"),
    path("reader/<int:pk>/", DocDetail.as_view(), name="doc-detail"),
]
