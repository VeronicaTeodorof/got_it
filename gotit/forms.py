from allauth.account.forms import SignupForm, LoginForm


class CustomSignupForm(SignupForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'auth-input'
        self.fields['email'].widget.attrs['class'] = 'auth-input'
        self.fields['password1'].widget.attrs['class'] = 'auth-input'
        self.fields['password2'].widget.attrs['class'] = 'auth-input'


class CustomLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['login'].widget.attrs['class'] = 'auth-input'
        self.fields['password'].widget.attrs['class'] = 'auth-input'
