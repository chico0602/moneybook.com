from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import (LoginView, LogoutView)
from django.views.generic import CreateView
from .forms import LoginForm, UserCreateForm
# Create your views here.


def top(request):
    return render(request, 'registration/top.html')


# ログイン
class Login(LoginView):
    form_class = LoginForm
    template_name = 'registration/login.html'


# ログアウト
class Logout(LoginRequiredMixin, LogoutView):
    template_name = 'registration/top.html'


# アカウント作成
class Create_account(CreateView):
    def post(self, request, *args, **kwargs):
        form = UserCreateForm(data=request.POST)
        if form.is_valid():
            form.save()
            # フォームから'username'を読み取る
            username = form.cleaned_data.get('username')
            # フォームから'password1'を読み取る
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')
        return render(request, 'registration/create.html', {'form': form})

    def get(self, request, *args, **kwargs):
        form = UserCreateForm(request.POST)
        return render(request, 'registration/create.html', {'form': form})
