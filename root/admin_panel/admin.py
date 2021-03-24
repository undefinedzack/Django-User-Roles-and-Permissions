from django.contrib import admin

from .models import Userz, Adminz

# Register your models here.
admin.site.register(Userz)
admin.site.register(Adminz)
