from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin
from .forms import RegisterForm, EmployeeForm, InventarForm
from .models import Employee, Inventar
from django.shortcuts import render
from django.views.generic import DetailView, CreateView


def main(request):
    return render(request, "main.html")


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()

            login(request, user)
            return redirect('/')
    else:
        form = RegisterForm()
    return render(request, 'registration/reg.html', {'form': form})


class MyDetailView1(DetailView):
    model = Inventar
    template_name = 'detail/detail.html'
    context_object_name = 'detail'
    slug_field = 'slug'


@login_required
def employee_forms(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee')
    else:
        form = EmployeeForm()
    return render(request, 'forms/employee_forms.html', {'form': form})


@login_required
def inventar_forms(request):
    if request.method == 'POST':
        form = InventarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inventar')
    else:
        form = InventarForm()
    return render(request, 'forms/inventar_forms.html', {'form': form})


@login_required
def employee(request):
    employees = Employee.objects.all()
    return render(request, 'employee.html', {'employees': employees})


@login_required
def inventar(request):
    inventars = Inventar.objects.all()
    return render(request, 'inventar.html', {'inventars': inventars})


@login_required
def inventar_AZ(request):
    inventars = Inventar.objects.order_by('name')
    return render(request, 'inventar.html', {'inventars': inventars})


@login_required
def inventar_ZA(request):
    inventars = Inventar.objects.order_by('-name')
    return render(request, 'inventar.html', {'inventars': inventars})


@login_required
def inventar_price(request):
    inventars = Inventar.objects.order_by('price')
    return render(request, 'inventar.html', {'inventars': inventars})


@login_required
def inventar_reprice(request):
    inventars = Inventar.objects.order_by('-price')
    return render(request, 'inventar.html', {'inventars': inventars})


@login_required
def profile(request):
    profile = request.user.profile
    booked = Inventar.objects.filter(user=request.user)
    return render(request, 'profile.html', {'profile': profile, 'booked': booked})
