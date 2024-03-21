from django.urls import path

from apps.logon.views import CustomLoginView
from django.contrib.auth.views import LogoutView


app_name = 'logon'

urlpatterns = [
   path('sign-in/', CustomLoginView.as_view(), name ='sign_in'),
   path('logout/', LogoutView.as_view(), name ='logout'),
]