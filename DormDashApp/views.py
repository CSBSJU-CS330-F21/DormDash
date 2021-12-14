from django.shortcuts import render, redirect
from django.forms import inlineformset_factory
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *
from django.views.generic import CreateView
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.views.generic import TemplateView
from django.urls import reverse_lazy
import logging

'''
def createaccount(request):
    form = CreateUserForm()
    #pull data from DB
    #Transform
    #Send Email
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/login")

    context = {'form':form}
    return render(request, 'createaccount.html', context)
'''

class SignUpView(TemplateView):
    template_name = 'signup.html'


class CustomerSignUpView(CreateView):
    model = User
    form_class = CustomerSignUpForm
    template_name = 'signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'customer'
        return super().get_context_data(**kwargs)
    
    def form_valid(self,form):
        user = form.save()
        login(self.request, user)
        return redirect('restaurant_list')
        
class DriverSignUpView(CreateView):
    model = User
    form_class = DriverSignUpForm
    template_name = 'signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'driver'
        return super().get_context_data(**kwargs)
    
    def form_valid(self,form):
        user = form.save()
        login(self.request, user)
        return redirect('driverorders')

class ProfileChangeView(UpdateView):
    model = User
    form_class = ProfileChangeForm
    template_name = 'editprofile.html'

    def get_object(self):
        return self.request.user
    
    def form_valid(self,form):
        self.success_url = 'profile.html'
        return super().form_valid(form)

class ProfileDeleteView(DeleteView):
    model = User
    sucess_url = reverse_lazy('login.html')
        

'''
        if self.request.user.is_customer:
            return self.request.user.customer
        else:
            return self.request.user.driver

    def form_valid(self, form):
        messages.success(self.request, 'profile updated with success!')
        self.success_url = self.request.POST.get('previous_page')
        return super().form_valid(form)
'''

def loginUser(request):
    #pull data from DB
    #Transform
    #Send Email
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("restaurant_list")
        else:
            messages.info(request, "Username or Password is incorrect")

    return render(request, 'login.html')

#logout button: <a href="{% url 'logout' %}">Logout</a>
def logoutUser(request):
    logout(request)
    return redirect("/login")
    
@login_required(login_url='login')
def driverorders(request):
    ordersList = Order.objects.all()
    return render(request, 'driverorders.html',{'ordersList':ordersList})

def orderdetails(request):
    return render(request, 'orderdetails.html')

@login_required(login_url='login')
def restaurant_list(request):
    restaurantlist = Restaurant.objects.all()
    return render(request, 'restaurant_list.html',{'restaurantlist':restaurantlist })

@login_required(login_url='login')
def menu_list(request):
    menulist = menuItem.objects.all()
    rn = request.GET.get('rn','')
    restaurant_list = {'rn' : rn}
    return render(request, 'menu_list.html',{'menulist':menulist, 'rn':rn})

@login_required
def profile(request):
    return render(request, 'profile.html')