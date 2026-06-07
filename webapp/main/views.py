from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from .forms import UserProfileForm
from django.contrib.auth.forms import PasswordChangeForm
from .models import ContactMessage
from news.models import Artiles  # добавьте импорт

def index(request):
    from news.models import Artiles
    latest_news = Artiles.objects.order_by('-date')[:3]
    return render(request, 'main/index.html', {'latest_news': latest_news})

def about(request):
    return HttpResponse("<h4>страница про нас</h4>")

@login_required
def profile(request):
    # Получаем новости текущего пользователя
    user_news = Artiles.objects.filter(author=request.user).order_by('-date')
    
    if request.method == 'POST':
        if 'update_profile' in request.POST:
            form = UserProfileForm(request.POST, instance=request.user)
            if form.is_valid():
                form.save()
                messages.success(request, 'Профиль успешно обновлен!')
                return redirect('profile')
        elif 'change_password' in request.POST:
            password_form = PasswordChangeForm(request.user, request.POST)
            if password_form.is_valid():
                user = password_form.save()
                update_session_auth_hash(request, user)
                messages.success(request, 'Пароль успешно изменен!')
                return redirect('profile')
            else:
                messages.error(request, 'Исправьте ошибки в форме')
    else:
        form = UserProfileForm(instance=request.user)
        password_form = PasswordChangeForm(request.user)
    
    return render(request, 'main/profile.html', {
        'form': form,
        'password_form': password_form,
        'user_news': user_news,  # передаем новости в шаблон
    })

def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            messages.success(request, 'Регистрация прошла успешно!')
            return redirect('home')
        else:
            messages.error(request, 'Исправьте ошибки в форме')
    else:
        form = UserCreationForm()
    
    return render(request, 'registration/register.html', {'form': form})

def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        ContactMessage.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )
        
        messages.success(request, f'Спасибо, {name}! Ваше сообщение отправлено.')
        return redirect('contacts')
    
    return render(request, 'main/contacts.html')