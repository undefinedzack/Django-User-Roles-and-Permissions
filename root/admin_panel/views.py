from django.shortcuts import render, redirect

from .models import Userz
from .forms import UserForm


def home(request, user_id):
    user = Userz.objects.all().filter(pk=user_id)
    context = {
        'key': user_id,
        'user': user[0],
    }

    return render(request, 'admin_panel/index.html', context)


def login(request):
    if request.method == 'POST':
        print(request.POST)
        username = request.POST['username']
        password = request.POST['password']

        users = Userz.objects.all().filter(username=username, password=password)
        if len(users) > 0:
            return redirect('App:home', user_id=users[0].pk)
        else:
            print('somethings wrong!')

    return render(request, 'admin_panel/login.html')


# def AdminLogin(request):
#     if request.method=='POST':
#         username = request.POST['username']
#         password = request.POST['password']
#
#         admins = Adminz.objects.all().filter(username=username, password=password)
#         print(admins,'hi there')
#         if len(admins)>0:
#             return redirect('App:home', user_id=admins[0].pk)
#         else:
#             print('somethings wrong')
#
#     return render(request, 'admin_panel/AdminLogin.html')

def addUser(request, id):
    user = Userz.objects.all().filter(pk=id)
    if request.method == 'POST':
        user = UserForm(request.POST)

        print(request.POST)
        print(user)

        if user.is_valid():
            user.save()
            return redirect('App:Add User', id=id)

    form = UserForm()
    context = {
        'form': form,
        'user': user[0],
        'key': id
    }
    return render(request, 'admin_panel/addUser.html', context)


def viewUsers(request, id):
    user = Userz.objects.all().filter(pk=id)
    users = Userz.objects.all()

    context = {
        'users': users,
        'user': user[0],
        'key': id
    }

    return render(request, 'admin_panel/allUsers.html', context)


def deleteUsers(request, id):
    users = Userz.objects.all()
    users = [user for user in users if user.id != id]
    user = Userz.objects.all().filter(pk=id)

    context = {

        'users': users,
        'user': user[0],
        'key': id
    }

    return render(request, 'admin_panel/deleteUser.html', context)


def deleteUserAction(request, id, return_id):
    user = Userz.objects.all().filter(pk=id)

    user.delete()

    return redirect('App:Delete Users', id=return_id )


def editUsers(request, id):
    users = Userz.objects.all()
    # users = [user for user in users if user.id != id]
    user = Userz.objects.all().filter(pk=id)

    context = {
        'users': users,
        'user': user[0],
        'key': id,
    }

    return render(request, 'admin_panel/editUser.html', context)


def editUserPage(request, id, return_key):
    user = Userz.objects.all().filter(pk=id)
    owner = Userz.objects.all().filter(pk=return_key)
    print(user)

    updateForm = UserForm(instance=user[0])

    if request.method == 'POST':
        form = UserForm(request.POST, instance=user[0])
        print(form)
        if form.is_valid():
            form.save()

            return redirect('App:Edit user', id=return_key)
        else:
            print('not working')

    context = {
        'form': updateForm,
        'user': owner[0],
        'user': owner[0],
        'key': id,
        'return_key': return_key
    }

    return render(request, 'admin_panel/editUserPage.html', context)


def viewStatistics(request, id):
    user = Userz.objects.all().filter(pk=id)
    context = {
        'user': user[0],
        'key': id
    }

    return render(request, 'admin_panel/viewStatistics.html', context)
