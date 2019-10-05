from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import View
from django.db.models import Count, Sum
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from django.contrib.auth.models import User
from orders.models import Order, OrderLineItem
from products.models import Product
from .serializers import ProductSerializer, MonthlyEarning
from django.db.models.functions import TruncMonth, TruncYear


def view_chart(View):
    def get(self, request, *args, **kwargs):
        return render(request, "chart.html")


def view_chart_orders(View):
    def get(self, request, *args, **kwargs):
        return render(request, "chart_orders.html")


class ChartData(APIView):

    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        # Load data from Database

        # data serializer to convert sql database in json
        product = Product.objects.all()
        serializer = ProductSerializer(product, many=True)
        product_data = serializer.data

        
        product_name = Product.objects.all().values("name", "quantity_sold").order_by('-quantity_sold')[0:5]

        list_product_name = list()
        quantity_product_sold = list()

        for name in product_name:
            list_product_name.append(name['name'])
            quantity_product_sold.append(name['quantity_sold'])

        # calculate total earning by month
        earnings_by_month = OrderLineItem.objects.annotate(month=TruncMonth(
            'date')).values('month').annotate(Sum('total'))

        months_in_earning = list()
        earning = list()

        for entry in earnings_by_month:
            months_in_earning.append(entry['month'])
            earning.append(entry['total__sum'])

        count_orders = Order.objects.all().count()
        count_users = User.objects.all().count()

        # calculate number of orders by months

        number_of_orders_by_month = Order.objects.annotate(month=TruncMonth(
            'date')).values('month').annotate(total=Count('orderlineitem'))

        months_in_orders = list()
        orders_by_months = list()

        for entry in number_of_orders_by_month:
            months_in_orders.append(entry['month'])
            orders_by_months.append(entry['total'])

        # calculate number of product sold by product an made a pie chart

        # Labels

        # Assign data
        data = {
            "number_of_orders_by_month": number_of_orders_by_month,
            "months_in_earning": months_in_earning,
            "earning": earning,
            "months_in_orders": months_in_orders,
            "orders_by_months": orders_by_months,
            "product_name": list_product_name,
            "quantity_product_sold": quantity_product_sold,
        }

        return Response(data)
