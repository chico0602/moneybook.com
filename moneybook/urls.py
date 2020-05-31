import django.contrib.auth.views
from django.urls import path,include
from . import views
from .views import index



app_name = 'moneybook'

urlpatterns = [
    path('', views.SpendingList.as_view(), name='history'),
    path('input/', views.SpendingCreate.as_view(), name='input'),
    path('s_detail/<int:pk>', views.SpendingDetail.as_view(), name='s_detail'),
    path('s_update/<int:pk>', views.SpendingUpdate.as_view(), name='s_update'),
    path('s_delete/<int:pk>', views.SpendingDelete.as_view(), name='s_delete'),
]