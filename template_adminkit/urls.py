"""
URL configuration for template_adminkit project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('apps.anon.urls','anon'), namespace='anon')),
    path('main/', include(('apps.main.urls','main'), namespace='main')),
    path('logon/', include(('apps.logon.urls','logon'), namespace='logon')),
    path('project/', include(('apps.project.urls','project'), namespace='project')),
    path('ETL/', include(('apps.ETL.urls','ETL'), namespace='ETL')),
    path('LLM/', include(('apps.LLM.urls','LLM'), namespace='LLM'))
]

handler404 = 'apps.error.views.error_404'
handler500 = 'apps.error.views.error_500'
handler403 = 'apps.error.views.error_403'
handler400 = 'apps.error.views.error_400'
