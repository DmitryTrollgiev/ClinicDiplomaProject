from django.urls import path

from . import views

urlpatterns = [
    path('edit/<int:record_id>', views.edit_record_info, name='edit_record_info'),
    path('add/<int:client_id>', views.add_record, name='add_record'),
]