from django.shortcuts import render


def index(request):
    context = {}

    return render(request, 'admin_panel/index.html', context)
