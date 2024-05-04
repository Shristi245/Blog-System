from django.urls import path
from users import views as user_views
from django.contrib.auth import views as auth_views
from .views import *


from django.contrib.auth.views import ( 

    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView
)

urlpatterns = [
    path('register/', register_user, name="register" ),
    path('profile/<str:username>/', user_views.profile, name='user_profile'),
    path('profile_update', user_views.profile_update, name="profile_update"),

    path('login/', loginUser, name='login'),
    path('logout', logoutUser, name='logout'),
    path('create/', create_post, name='create'),

    
    path('reset/', user_views.CustomPasswordResetView.as_view(), name='password_reset'),
    path('password-reset/', PasswordResetView.as_view(template_name='users/password_reset.html'),name='password-reset'),
    path('password-reset/done/', PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),name='password_reset_confirm'),
    path('password-reset-complete/',PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),name='password_reset_complete'),
  
]
