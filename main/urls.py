from django.urls import path
from . import views

urlpatterns = [
    
    path('signup/', views.signup_view, name='signup'),
    path('', views.signup_view, name='signup'),
    path('home/', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path("logout/", views.log_out, name="log_out"),
    path("delete/", views.delete, name="delete"),
    path("post/", views.ServiceRequestPage, name="ServiceRequestPage"),
    path("success/", views.success, name="success"),
    path("profile/", views.businessProfile, name="profile"),
    path("user/<str:username>/", views.viewProfile, name="viewProfile"),
    path('verify/', views.verificationCode, name='verificationCode'),
    path("review/", views.review, name="review"),
    

]



