from django.urls import path
from .views import login_view, register
from django.contrib.auth.views import LogoutView, PasswordChangeView, PasswordChangeDoneView
from django.urls import reverse_lazy

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
    path('register/', register, name='register'),
    path('password_change/', PasswordChangeView.as_view(
        template_name='accounts/password_change.html',
        success_url=reverse_lazy('password_change_done')
    ), name='password_change'),
    path('password-change-done/', PasswordChangeDoneView.as_view(
        template_name='accounts/password_change_done.html'
    ), name='password_change_done'),
]
