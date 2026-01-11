from django.urls import path, include
from . import views

app_name = 'users'

urlpatterns = [
    path('', views.user_page_view, name='user_page')
]