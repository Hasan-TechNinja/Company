from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Home, name = 'home'),
    path('snippets/', views.snippet_list),
    path('snippets/<int:pk>/', views.snippet_detail),
    path('registration/', views.Registration, name='registration'),
    path('login/', views.LoginView, name='login'),
    path('accounts/login/', views.LoginView, name='login'),
    path('logout/', views.LogoutView, name='logout'),
    path('company/', views.Company, name='company'),
]
