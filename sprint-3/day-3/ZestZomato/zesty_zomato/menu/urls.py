from django.urls import path
from . import views

urlpatterns = [
    path('dishes/', views.dish_list, name='dish_list'),
    path('add_dish/', views.add_dish, name='add_dish'),
    path('',views.home)
    # Define URLs for updating and deleting dishes
]
