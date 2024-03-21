from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

# Create your views here.
# Create your views here.
class IndexView(LoginRequiredMixin, TemplateView):
   template_name = 'app/main/index.html'

   def get_context_data(self, *args, **kwargs):
      context = super(IndexView,self).get_context_data(*args, **kwargs)
      dashboard_options = {
         'title': 'Inicio',
      }
      context['api'] = dashboard_options
      return context