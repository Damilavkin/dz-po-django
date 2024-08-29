from django.urls import path, include
from . import views


app_name = 'task2'

urlpatterns = [
    path('views1/', views.test_views1, name='test_views1'),
    path('views2/', views.test_views2, name='test_views2')
]