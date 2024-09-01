from django.shortcuts import render


def platform(request):
    return render(request, 'fourth_task/platform.html')


def games(request):
    context = {'games': ['Atomic Heart', 'Cyberpunk 2077', 'Baldur’s Gate III']}

    return render(request, 'fourth_task/games.html', context)


def cart(request):
    return render(request, 'fourth_task/cart.html')
