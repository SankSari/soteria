from django import forms


class RegisterForm(forms.Form):
    """Registeration form for Soteria
    """
    username = forms.CharField(max_length=150)
    name = forms.CharField(max_length=180)
    email = forms.EmailField()
    phone_number = forms.IntegerField(
        min_value=1000000000, max_value=9999999999)
    # Register as a volunteer
    volunteer = forms.BooleanField(required=False)
    # Password and retype password
    password1 = forms.CharField(max_length=128)
    password2 = forms.CharField(max_length=128)

    def clean(self):
        cleaned_data = super().clean()

        # Check if both the passwords are equal
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        if password1 != password2:
            raise forms.ValidationError(
                'The two passwords do not match each other.')


class LoginForm(forms.Form):
    """Login form for Soteria
    """
    username = forms.CharField(max_length=150)
    password = forms.CharField(max_length=128)
