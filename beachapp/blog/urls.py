from django.urls import path
from . import views

urlpatterns = [
    path('', views.log_in, name='log_in'), 
    path('sign_up', views.sign_up, name='sign_up'),
]