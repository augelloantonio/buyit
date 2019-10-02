from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import View


def view_chart(View):
    return render(request, "chart.html")


def get_data(request, *args, **kwargs):
    data = {
        "sales": 100,
        "customer": 10,
    }
    return JsonResponse(data)
