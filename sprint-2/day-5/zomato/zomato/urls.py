"""
URL configuration for zomato project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.dish_list,name="dish_list"),
    path('dish/<int:dish_id>/', views.dish_detail, name='dish_detail'),
    path('add/', views.add_dish, name='add_dish'),
    path('update/<int:dish_id>/', views.update_dish, name='update_dish'),
    path('delete/<int:dish_id>/', views.delete_dish, name='delete_dish'),

]
