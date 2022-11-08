from django.views.generic.base import TemplateView


class HomePage(TemplateView):
    template_name = "home/main.html"


class AboutPage(TemplateView):
    template_name: str = "home/about.html"
