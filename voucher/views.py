from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View
from django.contrib import messages
from orders.models import Order
from .models import Voucher
from .forms import VoucherForm
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
import datetime
from django.utils import timezone
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from .forms import AddNewVOucher


@require_POST
def add_voucher(request):
    user = request.user
    voucher_form = VoucherForm(request.POST)
    now = timezone.now()
    if voucher_form.is_valid():
        code = voucher_form.cleaned_data['code']
        print(user)
        if Order.objects.filter(voucher=code).filter(user=user).exists():
            messages.warning(
                request, 'Ops, you cannot use this voucher twice.')
        else:
            try:
                voucher = Voucher.objects.get(code=code,
                                              active=True)
                request.session['voucher_id'] = voucher.id
                messages.success(request, 'Coupon applied.')
            except Voucher.DoesNotExist:
                messages.warning(request, 'Coupon not accepted.')
                request.session['voucher_id'] = None
    return redirect("view_cart")


@login_required
def add_new_voucher(request):
    if request.method == "POST":
        form = AddNewVOucher(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(voucher_view)
    else:
        form = AddNewVOucher()
    return render(request, "dashboardaddavouchercode.html", {'form': form})


def edit_a_voucher(request, id):
    voucher = get_object_or_404(Voucher, pk=id)

    if request.method == "POST":
        form = AddNewVOucher(request.POST, instance=voucher)
        if form.is_valid():
            form.save()
            return redirect(voucher_view)
    else:
        form = AddNewVOucher(instance=voucher)
    return render(request, "dashboardaddavouchercode.html", {'form': form})


def voucher_view(request):
    vouchers = Voucher.objects.all()
    return render(request, 'dashboardvouchers.html', {'vouchers': vouchers})


def delete_voucher(request, pk):
    item = get_object_or_404(Voucher, pk=pk)
    item.delete()
    return redirect(voucher_view)
