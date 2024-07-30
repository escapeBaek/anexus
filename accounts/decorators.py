from django.contrib.auth.decorators import user_passes_test
from django.core.exceptions import PermissionDenied

def user_is_approved(function=None):
    """
    Decorator for views that checks that the logged in user is approved.
    """
    actual_decorator = user_passes_test(
        lambda u: u.is_authenticated and u.is_approved,
        login_url='login',
        redirect_field_name=None
    )
    if function:
        return actual_decorator(function)
    return actual_decorator
