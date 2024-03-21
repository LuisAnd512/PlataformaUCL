from django.urls import path
from apps.ETL.views import  IndexView

app_name = 'ETL'

urlpatterns = [
   path('', IndexView.as_view(), name ='index1'),
   ]