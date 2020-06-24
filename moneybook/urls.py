from django.urls import path
from . import views


app_name = 'moneybook'

urlpatterns = [
    path('history/', views.InputList.as_view(), name='history'),
    path('input/', views.InputCreate.as_view(), name='input'),
    path('s_detail/<int:pk>', views.SpendingDetail.as_view(), name='s_detail'),
    path('s_update/<int:pk>', views.SpendingUpdate.as_view(), name='s_update'),
    path('s_delete/<int:pk>', views.SpendingDelete.as_view(), name='s_delete'),
    path('analysis/', views.show_circle_grahp, name='analysis'),
    path('total_analysis/', views.show_total_grahp, name='total_analysis'),
]