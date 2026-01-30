from . import views
from django.urls import path
app_name='food'
urlpatterns = [

    path('', views.homepage, name='homepage'),
    path('menu/', views.menu, name='menu'),
    path('menu/add/', views.add_food, name='add_item'),
    path('menu/item/<int:id>/', views.detail, name='detail'),
]
