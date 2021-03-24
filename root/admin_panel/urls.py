from django.urls import path

from . import views

app_name = 'App'
urlpatterns = [
    path('home/<int:user_id>', views.home, name='home'),
    path('login/', views.login, name='Login'),

    path('addUser/')
]