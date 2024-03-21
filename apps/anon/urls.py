from django.urls import path

from apps.anon.views import HomeView, ContactsView


app_name = 'anon'

urlpatterns = [
   path('', HomeView.as_view(), name ='home'),
   path('contacts/', ContactsView.as_view(), name ='contacts'),
]