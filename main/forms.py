from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django_recaptcha.fields import ReCaptchaField

from .models import Inventar,Employee


class InventarForm(ModelForm):
    class Meta:
        model = Inventar
        fields = '__all__'
        exclude = ['slug']


class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        exclude = ['slug']




class RegisterForm(UserCreationForm):


    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

