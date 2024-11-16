from . import views 
from django.urls import path

urlpatterns = [
 path('set_name/', views.set_name, name='set_name'),
 path('get_name/', views.get_name, name='get_name'),
]