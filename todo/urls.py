from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('update/<str:pk>/', views.update_task, name='update'),
    path('delete/<str:pk>/', views.delete_task, name='delete'),
]