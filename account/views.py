from django.shortcuts import render
from .forms import LoginForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

# Create your views here.

@login_required
def dashboard(request):
    context = {'section': 'dashboard'}
    return render(request, 'account/dashboard.html', context=context)

def auth_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                username=cd['nickname'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse("Успешно вошли")
                else:
                    return HttpResponse("Вы забанены")
            else:
                return HttpResponse("Неправильный логин и/или пароль")
    else:
        form = LoginForm()
        context = {'form': form}
    return render(request, template_name='account/login.html', context=context)