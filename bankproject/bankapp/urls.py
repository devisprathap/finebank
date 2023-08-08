from . import views
from django.urls import path
app_name='bankapp'
urlpatterns = [

    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('form',views.form,name='form'),
    path('home',views.home,name='home'),
    path('branches',views.branches,name='branches'),
    path('branch1',views.branch1,name='branch1'),
    path('branch2',views.branch2,name='branch2'),
    path('branch3',views.branch3,name='branch3'),
    path('branch4',views.branch4,name='branch4')





]
