
from django.contrib import admin
from django.urls import path
from CRM import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.IndexPage,name="index"),
    path('Login/',views.LoginPage,name="Login"),
    path('Dash1/',views.dashboard,name="Dash1"),
]
