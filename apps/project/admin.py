from django.contrib import admin
from apps.project.models import *

# Register your models here.
admin.site.register(Project)
admin.site.register(Network)
admin.site.register(Data)
admin.site.register(Account)
admin.site.register(Schudele)