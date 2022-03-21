from django.urls import path

from . import views

urlpatterns = [
    path('mail/send/', views.index, name='index')
]