from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('about/', views.about, name="about"),
    path('contact', views.contact, name="contact"),
    path('register/', views.register, name="register"),
    path('login_page/', views.login_page, name="login_page"),
    path('logout_page/', views.logout_page, name="logout_page"),
    path('profile/', views.profile, name="profile"),
    path('admin_dashboard/', views.admin_dashboard, name="admin_dashboard"),
    path('customer/<str:pk>', views.customer, name="customer"),
    path('bus_dashboard/<str:pk>', views.bus_dashboard, name="bus_dashboard"),
    path('add_bus/', views.add_bus, name="add_bus"),
    path('add_custo/', views.add_custo, name="add_custo"),
    path('add_route/<str:pk>/', views.add_route, name="add_route"),
    path('add_booking/<str:pk>/', views.add_booking, name="add_booking"),
    path('cust_booking/', views.cust_booking, name="cust_booking"),
    path('user_page/', views.user_page, name="user_page"),
    path('allbooking/', views.allbooking, name="allbooking"),
]
