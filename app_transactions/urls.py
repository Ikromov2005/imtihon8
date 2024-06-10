from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.register, name='register'),
    path('create/', views.create_transaction, name='create_transaction'),
    path('update/<int:id>/', views.update_transaction, name='update_transaction'),
    path('delete/<int:id>/', views.delete_transaction, name='delete_transaction'),
]