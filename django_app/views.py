# django_app/views.py
from django.views.generic import TemplateView, ListView
from .models import Quote


# class HomePageView(TemplateView):
#     template_name = 'home.html'


class HomePageView(ListView):
    model = Quote
    template_name = 'home.html'
    context_object_name = 'all_quotes_list' # new


class AboutPageView(TemplateView):
    template_name = 'about.html'

