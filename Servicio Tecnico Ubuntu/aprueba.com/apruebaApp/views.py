from django.shortcuts import render

def renderIndex(request):
    return render(request, 'index.html')

def renderLogin(request):
    return render(request, 'login.html')
