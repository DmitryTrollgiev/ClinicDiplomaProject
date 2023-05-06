from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='clients'),
    path('view/<int:client_id>', views.view_client_info, name='view_client_info'),
    path('edit/<int:client_id>', views.edit_client_info, name='edit_client_info'),
    path('add/', views.add_client, name='add_client'),
]