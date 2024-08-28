from django.shortcuts import render


def test_views1(request):
    return render(request, 'second_task/for class views.html')


def test_views2(request):
    return render(request, 'second_task/for func views.html')

