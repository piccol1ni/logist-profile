from django.shortcuts import render

def authenticate_page(request):
    print(request.url)
    return render(request, 'authenticate/login.html')

def login_user(request):
    context = {}
    return render(request, 'authenticate/login.html', context)

def register_user(request):
    pass

def logout_user(request):
    pass
