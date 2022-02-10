from django.shortcuts import render



def register(request):
    template_name = 'accounts/register.html'
    context = {}
    return render(request, template_name, context)

def login(request):
    template_name = 'accounts/login.html'
    context = {}
    return render(request, template_name, context)

def logout(request):
    template_name = 'accounts/logout.html'
    context = {}
    return render(request, template_name, context)
