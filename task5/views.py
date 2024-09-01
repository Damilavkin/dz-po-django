from django.shortcuts import render
from .forms import UserRegister


users = ['user1', 'user2', 'user3']


def sign_up_by_django(request):
    info = {}
    if request.method == "POST":
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']
            if password == repeat_password and age >= 18 and username not in users:
                return render(request, 'fifth_task/registration_page.html',
                              {'message': f'Приветствуем, {username}!', 'form': UserRegister()})
            else:
                info['error'] = 'Пожалуйста, проверьте введенные данные.'
    else:
        form = UserRegister()

    return render(request, 'fifth_task/registration_page.html', {'form': form, 'info': info})


def sign_up_by_html(request):
    info = {}
    if request.method == "POST":
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']
            if password == repeat_password and age >= 18 and username not in users:
                return render(request, 'fifth_task/registration_page.html',
                              {'message': f'Приветствуем, {username}!', 'form': UserRegister()})
            else:
                info['error'] = 'Пожалуйста, проверьте введенные данные.'
    else:
        form = UserRegister()

    return render(request, 'fifth_task/registration_page.html', {'form': form, 'info': info})
