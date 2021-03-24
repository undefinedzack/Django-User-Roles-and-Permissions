from django.shortcuts import render, redirect

from .models import Adminz, Userz
from .forms import UserForm


def home(request, user_id):
    admin = Adminz.objects.all().filter(pk=user_id)
    print(admin)
    context = {
        'key' : user_id,
    }

    return render(request, 'admin_panel/index.html', context)


def login(request):
    if request.method == 'POST':
        print(request.POST)
        username = request.POST['username']
        password = request.POST['password']

        admins = Adminz.objects.all().filter(username=username, password=password)
        if len(admins) > 0:
            return redirect('App:home', user_id=admins[0].pk)
        else:
            print('somethings wrong!')

    context = {}

    return render(request, 'admin_panel/login.html', {})


def addUser(request):
    if request.method == 'POST':
        user = UserForm(request.POST)
        
