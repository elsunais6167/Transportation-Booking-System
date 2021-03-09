from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.db.models import Sum
from django.contrib.auth import authenticate, login, logout
from .forms import CreateBusForm
from .forms import CustomerForm
from .forms import RouteForm
from .forms import BookingForm
from .forms import CreateUserForm
from .forms import BookingCust
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .decorators import unauthenticated_user, allowed_users, admin_only

# Create your views here.

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')


@unauthenticated_user
def register(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            
            group = Group.objects.get(name='customer')
            user.groups.add(group)
            Customer.objects.create(
            user=user,
            )
            return redirect('login_page')
    context = {'form':form}

    return render(request, 'register.html', context)

@unauthenticated_user
def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('admin_dashboard')
        else:
            messages.info(request, 'Username or Passord is Incorrect!')
    context = {}
    return render(request, 'login.html', context)

def logout_page(request):
    logout(request)
    return redirect('login_page')

@login_required(login_url='login_page')
@allowed_users(allowed_roles=['customer'])
def profile(request):
    customer = request.user.customer
    form = CustomerForm(instance=customer)

    if request.method == 'POST':
        form = CustomerForm(request.POST, request.FILES, instance=customer)
        if form.is_valid():
            form.save()

    context = {'form': form}    
    return render(request, 'profile.html', context)

@login_required(login_url='login_page')
@admin_only
def admin_dashboard(request):
    customers = Customer.objects.all()
    bus = Bus.objects.all()
    routes = Routes.objects.all()
    booking = Booking.objects.all()
    tcus = customers.count()
    tbus = bus.count()
    tbook = booking.count()
    troute = routes.count()

    context = {'customers': customers, 'bus': bus, 'booking': booking, 'routes': routes, 'tcus': tcus, 'tbus': tbus, 'tbook': tbook, 'troute': troute} 
    return render(request, 'admin_dashboard.html', context)

@login_required(login_url='login_page')
@admin_only
def allbooking(request):
    booking = CusBooking.objects.all()

    context = {'booking': booking} 
    return render(request, 'allbooking.html', context)

@login_required(login_url='login_page')
@allowed_users(allowed_roles=['admin'])
def bus_dashboard(request, pk):
    bus = Bus.objects.get(id=pk)
    route = bus.routes_set.all()
    troute = route.count()
    context = {'bus': bus, 'route': route, 'troute': troute}
    return render(request, 'bus_dashboard.html', context)

@login_required(login_url='login_page')
def customer(request, pk):
    customer = Customer.objects.get(id=pk)
    book = customer.booking_set.all()

    abook = book.filter(status='Active Booking').count()
    ubook = book.filter(status='Used Booking').count()

    context = {'customer': customer, 'book': book, 'abook': abook, 'ubook': ubook}
    return render(request, 'cust_dashboard.html', context)

@login_required(login_url='login_page')
@allowed_users(allowed_roles=['admin'])
def add_bus(request):
    form = CreateBusForm()
    if request.method == "POST":
        form = CreateBusForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')

    context = {'form': form}

    return render(request, 'add_busForm.html', context)

@login_required(login_url='login_page')
@allowed_users(allowed_roles=['admin'])
def add_custo(request):
    form = CustomerForm()
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')

    context = {'form': form}

    return render(request, 'addCustom.html', context)

@login_required(login_url='login_page')
@allowed_users(allowed_roles=['admin'])
def add_route(request, pk):
    bus = Bus.objects.get(id=pk)
    form = RouteForm(initial={'bus': bus})
    if request.method == "POST":
        form = RouteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')
    context = {'form': form}

    return render(request, 'add_routeForm.html', context)

@login_required(login_url='login_page')
@allowed_users(allowed_roles=['admin'])
def add_booking(request, pk):
    customer = Customer.objects.get(id=pk)
    form = BookingForm(initial={'customer': customer})
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')
    context = {'form': form}

    return render(request, 'add_bookingForm.html', context)


@login_required(login_url='login_page')
@allowed_users(allowed_roles=['customer'])
def cust_booking(request):
    form = BookingCust()
    if request.method == "POST":
        form = BookingCust(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.user = request.user
            entry.save()
            return redirect('user_page')
    context = {'form': form}

    return render(request, 'cust_book.html', context)

@login_required(login_url='login_page')
@allowed_users(allowed_roles=['customer'])
def user_page(request):
    trip = Routes.objects.filter(status='Available')
    booking = request.user.customer.booking_set.all()
    abook = booking.filter(status='Active Booking').count()
    ubook = booking.filter(status='Used Booking').count()
    context = {'trip' : trip, 'booking': booking, 'abook': abook, 'ubook': ubook}
    return render(request, 'user.html', context)