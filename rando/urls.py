from django.urls import path     
from . import views

urlpatterns = [
   path('', views.rand),
   path('reset', views.reset)
]