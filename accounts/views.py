from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404
from django.contrib import messages, auth
from django.urls import reverse
from .forms import UserLoginForm, UserRegistrationForm
from django.template.context_processors import csrf
from django.contrib.auth.decorators import login_required
from orders.models import Order, OrderLineItem
from home.views import index
from django.contrib.auth import logout as django_logout



@login_required
def logout(request):
    django_logout(request)
    return  HttpResponseRedirect(reverse('index'))


def login(request):
    """A view that manages the login form"""
    if request.method == 'POST':
        user_form = UserLoginForm(request.POST)
        if user_form.is_valid():
            user = auth.authenticate(request.POST['username_or_email'],
                                     password=request.POST['password'])

            if user:
                auth.login(request, user)
                messages.error(request, "You have successfully logged in")

                if request.GET and request.GET['next'] !='':
                    next = request.GET['next']
                    print('fail')
                    return HttpResponseRedirect(next)
                else:
                    print('success')
                    return redirect(reverse('index'))
            else:
                print('fail')
                user_form.add_error(None, "Your username or password are incorrect")
    else:
        print('fail')
        user_form = UserLoginForm()

    args = {'user_form': user_form, 'next': request.GET.get('next', '')}
    return render(request, 'login.html', args)


@login_required
def profile(request):
    user = request.user

    orders = Order.objects.all()
    order_info = OrderLineItem.objects.all()
    # filtering order for user 
    user_orders = OrderLineItem.objects.filter(user=user).order_by('-date')

    return render(request, 'profile.html', {'user_orders':user_orders})


def register(request):
    """A view that manages the registration form"""
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            user_form.save()

            user = auth.authenticate(request.POST.get('email'),
                                     password=request.POST.get('password1'))

            if user:
                auth.login(request, user)
                messages.success(request, "You have successfully registered")
                return redirect(reverse('index'))

            else:
                messages.error(request, "unable to log you in at this time!")
    else:
        user_form = UserRegistrationForm()

    args = {'user_form': user_form}
    return render(request, 'register.html', args)