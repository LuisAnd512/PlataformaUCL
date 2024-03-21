from django.urls import path
from apps.LLM.views import  IndexView

app_name = 'LLM'

urlpatterns = [
   path('', IndexView.as_view(), name ='index'),
   ]