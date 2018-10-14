import functools

from django.shortcuts import redirect


def no_user_redirect_method(method):
    """If a user is not logged in, client is redirected to login page
    Use it for methods in class based views, as get() or post()
    """

    @functools.wraps(method)
    def wrapper(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/')
        return method(self, request, *args, *kwargs)

    return wrapper
