from django import forms
from .models import Voucher

class VoucherForm(forms.Form):
    code = forms.CharField()
    