from django.urls import path

from accounts.views import accounts

urlpatterns = [
    path('accounts/register/', accounts.RegisterView.as_view(), name='register'),
    path('accounts/change-password/', accounts.ChangePasswordView.as_view(), name='change_password'),
    path('accounts/me/', accounts.MeView.as_view(), name='me'),
]
