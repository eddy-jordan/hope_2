
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('tracking/', views.tracking, name='tracking'),
    path('track/<str:tracking_id>/', views.track_package, name='track_package'),
    path('track/', views.track_redirect, name='track_redirect'),  
     path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
