from allauth.account.forms import SignupForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group
from django import forms


class RegisterForm(UserCreationForm):
    email = forms.EmailField(label='Email')
    first_name = forms.CharField(label='Имя')
    last_name = forms.CharField(label='Фамилия')

    class Meta:
        model = User
        fields = ('username',
                  'first_name',
                  'last_name',
                  'email',
                  'password1',
                  'password2',)


class BaseSignupForm(SignupForm):
    def save(self, request):
        user = super(BaseSignupForm, self).save(request)
        base_group = Group.objects.get(name='common')
        base_group.user_set.add(user)
        return user
