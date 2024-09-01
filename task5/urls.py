from django.urls import path
from . import views


app_name = 'task5'
urlpatterns = [
    path('sign_up_django/', views.sign_up_by_django, name='sign_up_django'),
    path('sign_up_html/', views.sign_up_by_html, name='sign_up_html'),
]