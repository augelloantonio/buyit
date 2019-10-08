from django.shortcuts import render, redirect
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

@require_POST
def get_voucher(request):
    voucher_form = VoucherForm(request.POST)
    now = timezone.now()
    if voucher_form.is_valid():
        code = voucher_form.cleaned_data['code']
        try:
            voucher = Voucher.objects.get(code=code)
            request.session['voucher_id'] = voucher.id
            messages.success(request, 'Coupon Accepted.')
            return redirect("view_cart")
        except ObjectDoesNotExist:
            messages.success(request, 'Coupon Does not exist.')
            request.session['voucher_id'] = None
    else:
        voucher_form = VoucherForm()
    messages.error(request, 'Error')
    return redirect("view_cart")

