from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('register/',views.register,name='register'),
     path('login/',views.login_view,name='login'),
     path('logout/',views.logout_view,name='logout'),
    #   path('forgotpassword/',views.changepass,name='forgot'),
      path('forgot-password/',
         auth_views.PasswordResetView.as_view(
             template_name='authentication/password_reset_form.html',
             email_template_name='authentication/password_reset_email.html',
   
    success_url='/authentication/forgot-password/done/'
         ),
         name='password_reset'),

    path('forgot-password/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='authentication/password_reset_done.html'
             
         ),
         name='password_reset_done'),

    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='authentication/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),

    path('reset/done/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='authentication/password_reset_complete.html'
         ),
         name='password_reset_complete'),


]
