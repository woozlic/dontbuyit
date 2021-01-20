from django.shortcuts import render, redirect
from .forms import LoginForm, UserForm, ProfileForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Profile
from .forms import UserRegistrationForm

# Create your views here.


def auth_register(request):
    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # создаем пользовательский обьект, но пока не сохраняем
            new_user = user_form.save(commit=False)
            # устанавливаем пароль пользователю
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            # Profile.objects.create(user=new_user)
            print("аккаунт создан")
            return render(request, 'account/registration_done.html', {'new_user': new_user})
        else:
            print("ошибка заполнения формы")
    else:
        user_form = UserRegistrationForm()
    return render(request, 'account/register.html', {'user_form': user_form})

@login_required
def edit_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('account:dashboard')
        else:
            print("ошибка")
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)

    return render(request, 'account/edit_profile.html', {'user_form': user_form, 'profile_form': profile_form})

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