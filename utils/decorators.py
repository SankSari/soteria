import functools

from django.shortcuts import redirect


def logged_in_redirect_method(method):
    """If a user is not logged in, client is redirected to login page
    Use it for methods in class based views, as get() or post()
    """

    @functools.wraps(method)
    def wrapper(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/')
        return method(self, request, *args, *kwargs)

    return wrapper


def logged_in_redirect_func(func):
    """If a user is not logged in, client is redirected to login page
    Use it for non-class methods or functions
    """

    @functools.wraps(func)
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/')
        return func(request, *args, *kwargs)

    return wrapper
