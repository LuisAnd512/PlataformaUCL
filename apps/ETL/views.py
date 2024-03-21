
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.shortcuts import redirect
from django.contrib import messages
# Create your views here.

class IndexView(LoginRequiredMixin, TemplateView):
   template_name = 'app/ETL/index.html'
   def get_context_data(self, *args, **kwargs):
      context = super(IndexView,self).get_context_data(*args, **kwargs)
      context['api'] = {
            'title': 'ETL',
        }
      return context