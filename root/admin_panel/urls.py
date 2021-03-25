from django.urls import path

from . import views

app_name = 'App'
urlpatterns = [
    path('home/<int:user_id>', views.home, name='home'),
    path('login/', views.login, name='Login'),
    # path('adminLogin/', views.AdminLogin, name='Admin Login'),

    path('addUser/<int:id>', views.addUser, name='Add User'),
    path('allUsers/<int:id>', views.viewUsers, name='View Users'),
    path('deleteUser/<int:id>', views.deleteUsers, name='Delete Users'),
    path('deleteUserAction/<int:id>', views.deleteUserAction, name='Delete it'),
    path('editUser/<int:id>', views.editUsers, name='Edit user'),
    path('editUserPage/<int:id>', views.editUserPage, name='Edit user page'),
    path('viewStatistics/<int:id>', views.viewStatistics, name='view stats'),
]