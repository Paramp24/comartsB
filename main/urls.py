from django.urls import path
from . import views

urlpatterns = [
    
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('home/', views.home, name='home'),
    path("logout/", views.log_out, name="log_out"),
    path("delete/", views.delete, name="delete"),
    path("post/", views.ServiceRequestPage, name="ServiceRequestPage"),
    path("success/", views.success, name="success"),
    path("profile/", views.businessProfile, name="profile"),
    path("user/<str:username>/", views.viewProfile, name="viewProfile"),
    path('', views.signup_view, name='signup'),
    path('verify/', views.verificationCode, name='verificationCode'),
    path("review/", views.review, name="review"),
    
    #path("sendMail/", views.verify_email, name="verify_email"),   # need to delete in alittle while


]



