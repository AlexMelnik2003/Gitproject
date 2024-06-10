from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin
from .forms import RegisterForm, EmployeeForm, InventarForm, CategoryForm
from .models import Employee, Inventar, Category
from django.shortcuts import render
from django.views.generic import DetailView, CreateView, ListView
from django.db.models import Q


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

    def get_object(self, queryset=None):
        if queryset is None:
            queryset = self.get_queryset()
        obj = super().get_object(queryset=queryset)
        if obj.user != self.request.user:
            raise Http404("Нет записей")
        return obj

    def post(self, request, *args, **kwargs):

        self.object = self.get_object()

        if "delete" in request.POST:
            self.object.delete()

            return HttpResponseRedirect(reverse_lazy('inventar'))
        #
        return super().get(request, *args, **kwargs)


@login_required
def employee_forms(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            return redirect('employee')
    else:
        form = EmployeeForm()
    return render(request, 'employee_forms.html', {'form': form})


@login_required
def inventar_forms(request):
    if request.method == 'POST':
        form = InventarForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            return redirect('inventar')
    else:
        form = InventarForm()
    return render(request, 'inventar_forms.html', {'form': form})

@login_required
def category_forms(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            return redirect('categories')
    else:
        form = CategoryForm()
    return render(request, 'category_forms.html', {'form': form})

@login_required
def employee(request):
    employees = Employee.objects.all().filter(user=request.user)
    return render(request, 'employee.html', {'employees': employees})


@login_required
def inventar(request):
    inventars = Inventar.objects.all().filter(user=request.user)
    return render(request, 'inventar.html', {'inventars': inventars})


@login_required
def inventar_AZ(request):
    inventars = Inventar.objects.order_by('name').filter(user=request.user)
    return render(request, 'inventar.html', {'inventars': inventars})


@login_required
def inventar_ZA(request):
    inventars = Inventar.objects.order_by('-name').filter(user=request.user)
    return render(request, 'inventar.html', {'inventars': inventars})


@login_required
def inventar_price(request):
    inventars = Inventar.objects.order_by('price').filter(user=request.user)
    return render(request, 'inventar.html', {'inventars': inventars})


@login_required
def inventar_reprice(request):
    inventars = Inventar.objects.order_by('-price').filter(user=request.user)
    return render(request, 'inventar.html', {'inventars': inventars})


@login_required
def profile(request):
    profile = request.user.profile
    booked = Inventar.objects.filter(user=request.user)
    return render(request, 'profile.html', {'profile': profile, 'booked': booked})

@login_required
def SearchResultsView(request):
    query = request.GET.get('q')
    inventars = Inventar.objects.all().filter(
        Q(name__icontains=query)
    ).filter(user=request.user)
    return render(request, 'inventar.html', {'inventars': inventars})

@login_required
def categories(request):
    category = Category.objects.all().filter(user=request.user)
    return render(request, 'category.html', {'category': category})

def inventar_detail(request, category_id):
    category = get_object_or_404(Category, pk=category_id, user=request.user)
    inventars = Inventar.objects.filter(category=category, user=request.user)
    return render(request, 'inventar_detail.html', {'inventars': inventars, 'category': category})