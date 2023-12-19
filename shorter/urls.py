# shorter/urls.py

from django.urls import path
from .views import index, redirect_original, shorted

app_name = 'shorter'

urlpatterns = [
    path('', index, name='index'),
    path('<str:short_code>/', redirect_original, name='redirect_original'),
    path('shorted/<str:short_code>/', shorted, name='shorted'),
]
