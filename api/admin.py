from django.contrib import admin
from .models import Config, Cliente, Tarea
#from solo.admin import SingletonModelAdmin

admin.site.register(Config)
admin.site.register(Cliente)
admin.site.register(Tarea)
# Register your models here.
