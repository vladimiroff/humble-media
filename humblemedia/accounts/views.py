from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import LoginForm


def login(request):
    form = LoginForm(
        data=request.POST if request.method == 'POST' else None,
        request=request)

    if form.is_valid():
        return redirect('/')

    return render(request, 'login.html', locals())


@login_required
def logout(request):
    auth.logout(request)
    return redirect('/')
