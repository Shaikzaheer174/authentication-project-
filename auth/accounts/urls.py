#importing
from django.urls import path
from . import views
from django.contrib.auth import views as authview

#creating url
urlpatterns = [
    path('registration/',
        views.registration,name="Register"),
    #homepage
    path('',views.home,name="home"),
    #loginpage
    path('login/',authview.LoginView.as_view(template_name="login.html")),
    #logoutpage
    path('logout/',authview.LogoutView.as_view(template_name="logout.html")),
]
