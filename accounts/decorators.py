from django.contrib.auth.decorators import user_passes_test

def user_is_approved(function=None):
    """
    Decorator to check if the user is generally approved.
    """
    actual_decorator = user_passes_test(
        lambda u: u.is_authenticated and u.is_approved,
        login_url='login',
        redirect_field_name=None
    )
    if function:
        return actual_decorator(function)
    return actual_decorator

def user_is_specially_approved(function=None):
    """
    Decorator to check if the user has special approval for exams.
    """
    actual_decorator = user_passes_test(
        lambda u: u.is_authenticated and u.is_specially_approved,
        login_url='login',
        redirect_field_name=None
    )
    if function:
        return actual_decorator(function)
    return actual_decorator
