from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import View
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User


def view_chart(View):
    def get(self, request, *args, **kwargs):
        return render(request, "chart.html", {'customer': 10})


def get_data(request, *args, **kwargs):
    data = {
        "sales": 100,
        "customers": 10,
    }
    return JsonResponse(data)


class ChartData(APIView):

    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        count = User.objects.all().count()
        labels = ["Users", "Blue", "Yellow", "Green", "Purple", "Orange"]
        default_data = [count, 12, 32, 12, 33, 21]
        data = {
            "labels": labels,
            "default": default_data,
        }
        return Response(data)
