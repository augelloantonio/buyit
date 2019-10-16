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
def add_voucher(request):
    voucher_form = VoucherForm(request.POST)
    now = timezone.now()
    if voucher_form.is_valid():
        code = voucher_form.cleaned_data['code']
        try:
            voucher = Voucher.objects.get(code=code,
                                          active=True)
            request.session['voucher_id'] = voucher.id
            messages.success(request, 'Coupon applied.')
        except ObjectDoesNotExist:
            messages.warning(request, 'Coupon not accepted.')
            request.session['voucher_id'] = None
    return redirect("view_cart")
