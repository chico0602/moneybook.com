import django.contrib.auth.views
from django.urls import path,include
from . import views
from .views import index



app_name = 'moneybook'

urlpatterns = [
    path('', views.SpendingList.as_view(), name='history'),
    path('input/', views.SpendingCreate.as_view(), name='input'),
   # path('input/', views.spending_create, name='spending_create'),
   # path('create/send/', views.spending_create_send, name='spending_create_send'),
    
]