from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm
from django.shortcuts import render, redirect
# from users.models import Users
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User



def index(request):
    if 'user_id' in request.session:  # если пользователь не авторизован, отправляем на страницу входа
        return redirect('clients')

    data = {'error': ""}
    if request.method == 'POST':
        info = request.POST
        if info['email'] == "admin@gmail.com" and info['password'] == "admin":
            request.session['user_id'] = 1
            return redirect('clients')
        else:
            data['error'] = "Неправильный логин или пароль"


    form = LoginForm()
    data['form'] = form
    return render(request, 'login/index.html', data)


def logout(request):
    if 'user_id' in request.session.keys():
        del request.session['user_id']
    return redirect('login')