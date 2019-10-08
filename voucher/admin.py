from django.contrib import admin
from .models import Voucher

class VoucherAdmin(admin.ModelAdmin):
    model = Voucher

    
admin.site.register(Voucher, VoucherAdmin)