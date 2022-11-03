from django.urls import path
from .views import FAQIndex, ResourceList, ResourceDetail

app_name = "faq"
urlpatterns = [
    path("", FAQIndex.as_view(), name="faq-index"),
    path("resources/", ResourceList.as_view(), name="resource-list"),
    path("resources/<int:pk>/", ResourceDetail.as_view(), name="resource-detail"),
]
