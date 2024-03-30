from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .forms import UserForm


# Create your views here.
def index(request):
    return render(request, "index.html")




class UserRegister(CreateView):
    model = User
    template_name = 'registration/reg.html'
    form_class = UserForm
    success_url = reverse_lazy('login')
