from django.urls import path

from . import views

urlpatterns = [
    path('mail/send/', views.index, name='index'),
    path('server/', views.server_info, name='server_info'),
    path('server/detect/', views.server_detect, name='server_detect'),
    path('regex/', views.get_all_regex, name='regex'),
    path('regex/<int:item_id>/', views.get_regex, name='get_regex'),
    path('regex/create/', views.regex_create, name='regex_create'),
    path('regex/<int:item_id>/edit/', views.edit_regex, name='edit_regex'),
    path('regex/<int:item_id>/delete/', views.regex_delete, name='regex_delete'),
    path('regex/search/<str:query>/', views.regex_search, name='regex_search'),
]