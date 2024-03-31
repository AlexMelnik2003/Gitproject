from django.shortcuts import render, redirect
from .forms import RegisterForm
from .models import Employee, Inventar
from django.shortcuts import render
from django.views.generic import DetailView


def main(request):
    return render(request, "main.html")


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            users = form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'registration/reg.html', {'form': form})


class MyDetailView(DetailView):
    model = Inventar
    template_name = 'detail/detail.html'
    context_object_name = 'inventar'
    slug_field = 'slug'

def employee(request):
    employee = Employee.objects.all()
    return render(request, 'employee.html', {'employee': employee})

def inventar1(request):
    inventar = Inventar.objects.all()
    return render(request, 'inventar.html', {'inventar': inventar})
