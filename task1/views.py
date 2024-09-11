from django.shortcuts import render

from .forms import UserRegister


def platform(request):
    return render(request, 'first_task/platform.html')


def games(request):
    context = {'games': ['Atomic Heart', 'Cyberpunk 2077', 'Baldur’s Gate III']}

    return render(request, 'first_task/games.html', context)


def cart(request):
    return render(request, 'first_task/cart.html')


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

            if username in users:
                info['error'] = 'Пользователь с таким логином уже существует.'
            elif password != repeat_password:
                info['error'] = 'Пароли не совпадают.'
            elif age < 18:
                info['error'] = 'Возраст должен быть не менее 18 лет.'
            else:
                users.append(username)  # Добавляем нового пользователя
                return render(request, 'first_task/registration_page.html',
                              {'message': f'Приветствуем, {username}!', 'form': UserRegister()})

    else:
        form = UserRegister()

    return render(request, 'first_task/registration_page.html', {'form': form, 'info': info})


def sign_up_by_html(request):
    info = {}
    if request.method == "POST":
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            if username in users:
                info['error'] = 'Пользователь с таким логином уже существует.'
            elif password != repeat_password:
                info['error'] = 'Пароли не совпадают.'
            elif age < 18:
                info['error'] = 'Возраст должен быть не менее 18 лет.'
            else:
                users.append(username)  # Добавляем нового пользователя
                return render(request, 'first_task/registration_page.html',
                              {'message': f'Приветствуем, {username}!', 'form': UserRegister()})

    else:
        form = UserRegister()

    return render(request, 'first_task/registration_page.html', {'form': form, 'info': info})

