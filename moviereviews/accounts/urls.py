from django.urls import path

from accounts import views

urlpatterns = [
    path('', views.signupaccount, name='signupaccount'),
    path('logout/', views.logoutaccount, name='logoutaccount'),
    path('login', views.loginaccount, name='loginaccount'),
]