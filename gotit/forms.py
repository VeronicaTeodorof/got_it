from allauth.account.forms import SignupForm, LoginForm


class CustomSignupForm(SignupForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'auth-input'
        self.fields['username'].widget.attrs[
            'placeholder'] = 'username required'
        self.fields['email'].widget.attrs['class'] = 'auth-input'
        self.fields['email'].widget.attrs['placeholder'] = 'email required'
        self.fields['password1'].widget.attrs['class'] = 'auth-input'
        self.fields['password1'].widget.attrs[
            'placeholder'] = 'password required'
        self.fields['password2'].widget.attrs['class'] = 'auth-input'
        self.fields['password2'].widget.attrs[
            'placeholder'] = 'password again required'


class CustomLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['login'].widget.attrs['class'] = 'auth-input'
        self.fields['login'].widget.attrs['placeholder'] = 'email required'
        self.fields['password'].widget.attrs['class'] = 'auth-input'
        self.fields['password'].widget.attrs[
            'placeholder'] = 'password required'
