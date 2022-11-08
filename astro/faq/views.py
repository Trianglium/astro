from .models import Resource, AstroPoint
from django.views.generic import ListView, DetailView
from django.views.generic.base import TemplateView


class FAQIndex(ListView):
    model = AstroPoint
    template_name = "faq/faq_index.html"

    def get_context_data(self, **kwargs):
        context = super(FAQIndex, self).get_context_data(**kwargs)

        context["planet_list"] = AstroPoint.objects.filter(tag="planet")
        context["house_list"] = AstroPoint.objects.filter(tag="house")
        context["sign_list"] = AstroPoint.objects.filter(tag="sign")
        context["element_list"] = AstroPoint.objects.filter(tag="element")
        context["modality_list"] = AstroPoint.objects.filter(tag="modality")
        context["concept_list"] = AstroPoint.objects.filter(tag="concept")
        context["quality_list"] = AstroPoint.objects.filter(tag="quality")
        context["aspect_list"] = AstroPoint.objects.filter(tag="aspect")
        context["polarity_list"] = AstroPoint.objects.filter(tag="polarity")
        context["point_list"] = AstroPoint.objects.filter(tag="point")

        return context


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
