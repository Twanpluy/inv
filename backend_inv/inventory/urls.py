from django.urls import path
from .views import AddCatergorie

urlpatterns = [
    path('inventory/add-catergorie', AddCatergorie.as_view() ),
    ]
