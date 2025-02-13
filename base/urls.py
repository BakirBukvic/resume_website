from django.urls import path
from .views import welcome

app_name = 'base'

urlpatterns = [
    path('', welcome, name='welcome'),
]