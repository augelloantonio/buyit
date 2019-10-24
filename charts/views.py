from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from django.db.models import Count, Sum
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from orders.models import Order, OrderLineItem
from products.models import Product
from reviews.models import Review
from django.db.models.functions import TruncMonth, TruncYear, TruncDay
from itertools import groupby
from operator import itemgetter
from django.contrib.auth.decorators import login_required
from datetime import datetime, timedelta


def view_chart(View):
    def get(self, request, *args, **kwargs):
        return render(request, "chart.html")


def view_chart_orders(View):
    def get(self, request, *args, **kwargs):
        return render(request, "chart_orders.html")
