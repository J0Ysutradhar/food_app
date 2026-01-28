from . import views
from django.urls import path
app_name='food'
urlpatterns = [

    path('', views.homepage, name='homepage'),
]
