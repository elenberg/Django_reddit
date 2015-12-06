from django import forms
from django.contrib.auth.models import User

class RegistrationForm(forms.ModelForm):
    '''
    Form for registering a new account.
    '''
    username = forms.CharField(widget=forms.TextInput, label="Username")
    password1 = forms.CharField(widget=forms.PasswordInput,
                                label="Password")
    password2 = forms.CharField(widget=forms.PasswordInput,
                                label="Password (again)")

    class Meta:
        model = User
        fields = ['username' , 'password1', 'password2']

    def clean(self):
        '''
        Verifies that the values entered in the password field match
        '''

        cleaned_data = super(RegistrationForm, self).clean()
        if 'password1' in cleaned_data and 'password2' in cleaned_data:
            if cleaned_data['password1'] != cleaned_data['password2']:
                raise forms.ValidationError("Passwords don't match. Please enter both fields again.")
        return cleaned_data

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user