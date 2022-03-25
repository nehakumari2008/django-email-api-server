from django.urls import path

from . import views

urlpatterns = [
    path('mail/send/', views.index, name='index'),
    path('server/', views.server_info, name='server_info'),
    path('server/detect/', views.server_detect, name='server_detect'),
]