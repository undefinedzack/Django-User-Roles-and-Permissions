from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('admin_panel.urls')),
    path('admin/', admin.site.urls),
]
