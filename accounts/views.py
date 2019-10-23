from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404, reverse
from django.contrib import messages, auth
from django.urls import reverse
from .forms import UserLoginForm, UserRegistrationForm
from django.template.context_processors import csrf
from django.contrib.auth.decorators import login_required
from orders.models import Order, OrderLineItem
from home.views import index
from django.core.paginator import Paginator
from django.contrib.auth import logout as django_logout
from orders.filters import OrdersFilter


@login_required
def profile(request):
    user = request.user

    orders = Order.objects.all()
    order_info = OrderLineItem.objects.all()
    # filtering order for user
    user_orders = OrderLineItem.objects.filter(user=user).order_by('-id')
    # pagination
    paginator = Paginator(user_orders, 6)
    page = request.GET.get('page')
    pagination_orders = paginator.get_page(page)

    # Filter Orders
    filter_orders = OrdersFilter(request.GET, queryset=orders)

    months = [i.month for i in Order.objects.values_list(
        'date', flat=True).distinct()]
    months_filtered = list(dict.fromkeys(months))

    return render(request, 'profile.html', {'pagination_orders': pagination_orders, 'filter': filter_orders,
                                            'months_filtered': months_filtered})


def logout(request):
    """A view that logs the user out and redirects back to the index page"""
    auth.logout(request)
    messages.success(request, 'You have successfully logged out')
    return redirect(reverse('index'))


def personal_login(request):
    if request.user.is_authenticated:
        return redirect(reverse('profile'))
    else:
        return login(request)


def login(request):
    if request.method == 'POST':
        user_form = UserLoginForm(request.POST)
        if user_form.is_valid():
            user = auth.authenticate(request.POST['username_or_email'],
                                     password=request.POST['password'])

            if user:
                auth.login(request, user)
                messages.error(request, "You have successfully logged in")

                if request.GET and request.GET['next'] != '':
                    next = request.GET['next']
                    return HttpResponseRedirect(next)
                else:
                    return redirect(reverse('index'))
            else:
                user_form.add_error(
                    None, "Your username or password are incorrect")
    else:
        user_form = UserLoginForm()

    args = {'user_form': user_form, 'next': request.GET.get('next', '')}
    return render(request, 'login.html', args)


def register(request):
    """A view that manages the registration form"""
    if request.user.is_authenticated:
        return redirect(reverse('profile'))
    else:
        if request.method == 'POST':
            user_form = UserRegistrationForm(request.POST)
            if user_form.is_valid():
                user_form.save()

                user = auth.authenticate(request.POST.get('email'),
                                         password=request.POST.get('password1'))

                if user:
                    auth.login(request, user)
                    messages.success(
                        request, "You have successfully registered")
                    return redirect(reverse('index'))

                else:
                    messages.error(
                        request, "unable to log you in at this time!")
        else:
            user_form = UserRegistrationForm()

    args = {'user_form': user_form}
    return render(request, 'register.html', args)
