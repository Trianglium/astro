from django.views.generic.base import TemplateView
import pyaztro


class HomePage(TemplateView):
    template_name = "home/main.html"

    def get_context_data(self, **kwargs):
        context = super(HomePage, self).get_context_data(**kwargs)
        horoscopes = [pyaztro.Aztro(sign="aries"), pyaztro.Aztro(sign="taurus"), pyaztro.Aztro(sign="gemini"), pyaztro.Aztro(sign="cancer"), pyaztro.Aztro(sign="leo"), pyaztro.Aztro(sign="virgo"), pyaztro.Aztro(sign="libra"), pyaztro.Aztro(sign="scorpio"), pyaztro.Aztro(sign="sagittarius"), pyaztro.Aztro(sign="capricorn"), pyaztro.Aztro(sign="aquarius"), pyaztro.Aztro(sign="pisces")]
        context['horoscopes'] = horoscopes
        return context




    def todaysHoroscope(self):
        horoscope = pyaztro.Aztro(sign='aries')
        horoscope.description



class AboutPage(TemplateView):
    template_name: str = "home/about.html"
