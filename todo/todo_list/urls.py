from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('delete/<list_id>', views.delete, name="delete"),
    path('uncleared/<list_id>', views.uncleared, name="uncleared"),
    path('cleared/<list_id>', views.cleared, name="cleared"),
]
