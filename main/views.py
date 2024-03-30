from django.shortcuts import render
from .models import Employee, Inventar
from django.contrib.auth.models import User
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView
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


class MyDetailView(DetailView):
    model = Inventar
    template_name = 'detail/detail.html'
    context_object_name = 'inventar'
    slug_field = 'slug'