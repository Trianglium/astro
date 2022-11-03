from .models import Resource
from django.views.generic import ListView, DetailView
from django.views.generic.base import TemplateView


class FAQIndex(TemplateView):
    template_name = "faq/faq_index.html"


class ResourceList(ListView):
    model = Resource
    template_name = "faq/resource_list.html"
    context_object_name = "resource_list"

    def get_queryset(self):
        resources = Resource.objects.all()
        return resources.order_by("-title")


class ResourceDetail(DetailView):
    model = Resource
    template_name = "faq/resource_detail.html"
