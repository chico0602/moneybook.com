from django.urls import path
from . import views


app_name = 'accounts'

urlpatterns = [
    path('test_login/', views.guestlogin, name='test_login'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('create/', views.UserCreate.as_view(), name='create'),
    path('create/done', views.UserCreateDone.as_view(), name='create_done'),
    path('create/complete/<token>/', views.UserCreateComplete.as_view(), name='create_complete'),
    path('user_detail/<int:pk>/', views.UserDetail.as_view(), name='user_detail'),
    path('user_update/<int:pk>/', views.UserUpdate.as_view(), name='user_update'),
    path('top/', views.top, name='top'),
]
