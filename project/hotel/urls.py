from . import views
from django.urls import path, include
app_name='hotel'
urlpatterns = [

    path('', views.homepage, name='homepage'),
]
