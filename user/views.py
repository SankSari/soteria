from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login, logout
from utils.decorators import logged_in_redirect_method
from .forms import RegisterForm, LoginForm
from .models import User


class RegisterView(View):
    """Registeration as view
    """

    template_name = 'forms/register.html'
    form_class = RegisterForm
    model_class = User

    @logged_in_redirect_method
    def get(self, request):
        return render(request, self.template_name)

    @logged_in_redirect_method
    def post(self, request):
        form = self.form_class(request.POST)
        reg_err = None

        if form.is_valid():
            reg_err = self.form_valid(form, request)

            if reg_err is None:
                return redirect('/user/login/')

        self.form_invalid(form, request)
        return render(request, self.template_name, {'form': form, 'reg_err': reg_err})

    def form_valid(self, form, request):
        """Executes when the form is valid
        """
        data = form.data

        # Password hashing
        password = make_password(data.get('password1'))

        # Checkbox has value 'on' instead of True
        volunteer = False
        flag = data.get('volunteer')
        if flag is not None and flag != 'false' and flag != 'False':
            volunteer = True

        # Break first_name and last_name
        names = data.get('name').strip().split(' ')
        first_name = names[0]
        last_name = ""
        if len(names) > 1:
            last_name = ' '.join(names[1:])

        reg_err = self.register(data.get('username'), data.get('email'), data.get(
            'phone_number'), volunteer, password, first_name, last_name)
        return reg_err

    def form_invalid(self, form, request):
        """Executes when the form is invalid
        """
        return

    def register(self, username, email, phone_number, volunteer, password, first_name, last_name=""):
        """Puts user data into DB
        """

        try:
            new_user = User(username=username, email=email, phone_number=phone_number,
                            password=password, volunteer=volunteer, first_name=first_name,
                            last_name=last_name)
            new_user.save()
            return None
        except Exception as e:
            return e.__str__()


class LoginView(View):
    """Login as view
    """

    template_name = 'forms/login.html'
    form_name = LoginForm
    model_class = User

    @logged_in_redirect_method
    def get(self, request):
        return render(request, self.template_name)

    @logged_in_redirect_method
    def post(self, request):
        form = LoginForm(request.POST)
        auth_err = None

        if form.is_valid():
            auth_err = self.form_valid(form, request)

            if auth_err is None:
                return redirect('/')

        self.form_invalid(form, request)
        return render(request, self.template_name, {'form': form, 'auth_err': auth_err})

    def form_valid(self, form, request):
        """Executes when the form is valid
        """
        data = form.data

        user = authenticate(request=request, username=data.get(
            'username'), password=data.get('password'))
        if user is None:
            return 'Incorrect Username or Password'

        login(request, user)
        return

    def form_invalid(self, form, request):
        """Executes when the form is invalid
        """
        return


def logout_view(request):
    """Logour current user if any
    """

    logout(request)
    return redirect('/user/login/')
