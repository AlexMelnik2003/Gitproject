from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import Inventar


class BookForm(ModelForm):
    class Meta:
        model = Inventar
        fields = '__all__'
        exclude = ['slug']


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "password1", "password2")
