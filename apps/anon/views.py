from django.views.generic import TemplateView

# Create your views here.
class HomeView(TemplateView):
   template_name = 'public/index.html'
   
class ContactsView(TemplateView):
   template_name = 'public/contacts.html'