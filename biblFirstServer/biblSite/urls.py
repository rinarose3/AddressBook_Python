from django.urls import path

from .views import *

urlpatterns = [
    path('', bibl_main, name="main"),
    path('add/', bibl_add, name="add"),
    path('change/', bibl_change, name="change"),
    path('api/v1/ablist/', AddressBookAPIView.as_view(), name="ablist")
]