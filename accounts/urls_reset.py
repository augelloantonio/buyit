from django.urls import re_path, reverse_lazy
from django.contrib.auth.views import (
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
)

urlpatterns = [
    re_path(
        r'^$',
        PasswordResetView.as_view(success_url=reverse_lazy('password_reset_done')),
        name='password_reset'
    ),
    re_path(
        r'^done/$',
        PasswordResetDoneView.as_view(),
        name='password_reset_done'
    ),
    re_path(
        r'^(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',
        PasswordResetConfirmView.as_view(success_url=reverse_lazy('password_reset_complete')),
        name='password_reset_confirm'
    ),
    re_path(
        r'^complete/$',
        PasswordResetCompleteView.as_view(),
        name='password_reset_complete'
    ),
]
