from django.contrib import admin
from .models import Review

class ReviewAdmin(admin.ModelAdmin):
    model = Review
    list_display = ('product', 'rating', 'comment', 'pub_date', 'user')
    list_filter = ['pub_date', 'product', 'rating']
    search_fields = ['comment']
    
admin.site.register(Review, ReviewAdmin)
