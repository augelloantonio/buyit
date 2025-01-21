from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404, reverse
from django.contrib import messages, auth
from django.contrib.auth.forms import PasswordChangeForm
from django.urls import reverse
from django.contrib.auth.models import User
from .forms import UserLoginForm, UserRegistrationForm, EditUserForm
from django.template.context_processors import csrf
from django.contrib.auth.decorators import login_required
from orders.models import Order, OrderLineItem
from home.views import index
from django.core.paginator import Paginator
from django.contrib.auth import logout as django_logout, update_session_auth_hash
from django.core.mail import EmailMessage
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .filters import OrdersFilter
from utils import languageUtils


@login_required
def profile(request):
    user = request.user

    order_info = OrderLineItem.objects.all()
    # filtering order for user
    user_orders = OrderLineItem.objects.filter(user=user).order_by('-id')

    # Filter Orders
    filter_orders = OrdersFilter(request.GET, queryset=user_orders)
    user_order_list = filter_orders.qs

    # pagination to switch before filter order to work
    paginator = Paginator(user_order_list, 6)
    page = request.GET.get('page')

    try:
        pagination_orders = paginator.page(page)
    except PageNotAnInteger:
        pagination_orders = paginator.page(1)
    except EmptyPage:
        pagination_orders = paginator.page(paginator.num_pages)

    months = [i.month for i in Order.objects.values_list(
        'date', flat=True).distinct()]
    months_filtered = list(dict.fromkeys(months))
    
    translations = languageUtils.load_translations()

    return render(request, 'profile.html', {'pagination_orders': pagination_orders, 'filter': filter_orders, 'translations':translations})


def logout(request):
    """A view that logs the user out and redirects back to the index page"""
    auth.logout(request)
    messages.success(request, 'You have successfully logged out')
    return redirect(reverse('index'))


def login(request):
    if request.user.is_authenticated:
        return redirect(reverse('profile'))
    else:
        if request.method == 'POST':
            user_form = UserLoginForm(request.POST)
            if user_form.is_valid():
                user = auth.authenticate(request.POST['username_or_email'],
                                         password=request.POST['password'])

                if user:
                    auth.login(request, user)
                    messages.success(
                        request, "You have successfully logged in")

                    if request.GET and request.GET['next'] != '':
                        next = request.GET['next']
                        return HttpResponseRedirect(next)
                    else:
                        return redirect(reverse('profile'))
                else:
                    user_form.add_error(
                        None, "Your username or password are incorrect")
            else:
                user_form = UserLoginForm()
        else:
            user_form = UserLoginForm()

        translations = languageUtils.load_translations()
        
        args = {'user_form': user_form, 'next': request.GET.get('next', ''), 'translations':translations}
        
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
                    email = request.user.email
                    html_content = '<p>Welcome to <a href="https://buyit-platform.herokuapp.com/">Buyit</a>, enjoy your shopping, use the voucher code <strong>welcomenew</strong> and enjoy your 5% OFF of discount.</p>'
                    email = EmailMessage('Welcome', html_content, to=[email])
                    email.send()
                    messages.success(
                        request, "You have successfully registered, an email has been sent to you.")
                    return redirect(reverse('profile'))
                else:
                    messages.warning(
                        request, "unable to log you in at this time!")
        else:
            user_form = UserRegistrationForm()

    translations = languageUtils.load_translations()

    args = {'user_form': user_form, 'translations':translations}
    return render(request, 'register.html', args)


@login_required
def edit_profile(request):
    ''' view to edit a users profile '''

    if request.method == 'POST':
        # get an instance of the edit profile form
        form = EditUserForm(request.POST, instance=request.user)
        # set someone_has_this initially to false
        someone_has_this = False
        # if the email field or the username field
        # or both fields were changed do the following
        if "email" in form.changed_data or "username" in form.changed_data:
            # if the email field was changed do the following
            if "email" in form.changed_data:
                # the email input from the form
                form_email = request.POST['email']
                # a filter of all users with the same email
                # address as what was posted in the form
                filter_emails = User.objects.filter(email=form_email)
                # for all users with the same email
                # address as what was posted in the form
                for filter_email in filter_emails:
                    # if the email address is associated
                    # with another user id
                    if filter_email.id != request.user.id:
                        # set someone_has_email to True
                        someone_has_this = True
                        # display a message to say someone
                        # has this email address
                        messages.warning(request,
                                         'Somebody with this email address '
                                         'is already registered please enter '
                                         'a unique email address')
                        # return to the edit profile page
                        return redirect(reverse('edit_profile'))
            # if the username field has been changed do the following
            if "username" in form.changed_data:
                # the username input from the form
                form_username = request.POST['username']
                # a filter of all users with the same
                # username as what was posted in the form
                filter_usernames = User.objects.filter(
                    username=form_username)
                # for all users with the same username as
                # what was posted in the form
                for filter_username in filter_usernames:
                    # if the username is associated with another user id
                    if filter_username.id != request.user.id:
                        # set someone has this to True
                        someone_has_this = True
                        # otherwise display a message to say someone
                        # has this username
                        messages.warning(request,
                                         'Somebody already has this username '
                                         'please enter a unique username')
                        # return to the edit profile page
                        return redirect(reverse('edit_profile'))
        # if the form is valid and nobody has the same email
        # address or username save the form and redirect back
        # to the user profile
        if form.is_valid() and someone_has_this is False:
            form.save()
            messages.success(request,
                             'Your profile info have been updated!'
                             )
            return redirect('profile')
        else:
            # otherwise display an error message
            messages.warning(request,
                             'Invalid form please try again')
            # return to the edit profile page
            return redirect(reverse('edit_profile'))
    else:
        form = EditUserForm(instance=request.user)
        translations = languageUtils.load_translations()

        return render(request, 'editprofile.html', {'form': form, 'translations':translations})


@login_required
def change_password(request):
    '''Change User Password personal view'''
    if request.method == 'POST':
        # get an instance of the edit password form
        form = PasswordChangeForm(request.user, request.POST)
        # check if form is valid
        if form.is_valid():
            # if form is valid update password
            user = form.save()
            update_session_auth_hash(request, user)
            # get a message to advise the user that the password has been changed
            messages.success(request, (
                'Your password was successfully updated!'))
            # redirect to user page
            return redirect('profile')
        else:
            # if error will advise the user of the error
            messages.warning(request, ('Please correct the error below.'))
    else:
        # if form is not valid will return on edit profile page
        # and return the form
        form = PasswordChangeForm(request.user)
        
    translations = languageUtils.load_translations()
    return render(request, 'editpassword.html', {'form': form, 'translations':translations})
