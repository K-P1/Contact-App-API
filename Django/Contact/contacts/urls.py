from django.urls import path
from .views import CreateContactView, GetContactView, UpdateContactView, DeleteContactView

urlpatterns = [
    path('create_contact/', CreateContactView.as_view(), name='create_contact'),
    path('get_all_contact/', GetContactView.as_view(), name='get_all_contact'),
    path('get_contact/<str:id>/', GetContactView.as_view(), name='get_contact_by_id'),
    path('update_contact/<str:id>/', UpdateContactView.as_view(), name='update_contact'),
    path('delete_contact/<str:id>/', DeleteContactView.as_view(), name='delete_contact'),
]