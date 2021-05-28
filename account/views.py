from django.shortcuts import render, redirect, get_object_or_404
from .forms import LoginForm, UserForm, ProfileForm, DashboardForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Profile
from .forms import UserRegistrationForm, ProfileForm
from django.contrib import messages
import os


def auth_register(request):
    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():  # проверка на правильность формы
            if User.objects.filter(email=user_form.cleaned_data['email']).exists():
                messages.error(request, 'Данный email адрес уже зарегистрирован.')
            elif User.objects.filter(profile__phone_number=str(profile_form.cleaned_data['phone_number'])).exists():
                raise messages.error(request, 'Такой номер телефона уже зарегистрирован')
            else:
                # создаем пользовательский обьект, но пока не сохраняем
                new_user = user_form.save(commit=False)
                # устанавливаем пароль пользователю
                new_user.set_password(user_form.cleaned_data['password'])
                new_user.save()
                gender = profile_form.cleaned_data['gender']

                phone_number = profile_form.cleaned_data['phone_number']
                new_user.profile.gender = gender
                new_user.profile.phone_number = phone_number
                new_user.profile.save()
                return render(request, 'account/registration_done.html',
                              {'new_user': new_user})
        else:
            pass
    else:
        user_form = UserRegistrationForm()
        profile_form = ProfileForm()
    return render(request, 'account/register.html', {'user_form': user_form, 'profile_form': profile_form})


@login_required
def edit_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            messages.success(request, 'Данные профиля были обновлены!')
            # return redirect('account:dashboard')
        else:
            messages.error(request, 'Не удалось сохранить данные профиля.')
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)

    return render(request, 'account/edit_profile.html', {'user_form': user_form, 'profile_form': profile_form})


@login_required
def dashboard(request):
    if request.method == 'POST':
        form = DashboardForm(request.POST, request.FILES)
        if form.is_valid():
            print('form is valid')
            user_profile = Profile.objects.get(pk=request.user.profile.pk)
            old_image_path = user_profile.image.path
            if os.path.exists(old_image_path):
                os.remove(old_image_path)

            new_image = request.FILES['image']
            user_profile.image = new_image
            user_profile.save()
            messages.success(request, 'Вы успешно обновили фотографию в профиле')
            return redirect('account:dashboard')
    else:
        form = DashboardForm()
    context = {'section': 'dashboard', 'form': form}
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


@login_required
def user_detail(request, nickname):
    user = get_object_or_404(User, username=nickname)
    if user == request.user:
        return redirect('account:dashboard')
    return render(request, 'account/user_detail.html', {'user': user})