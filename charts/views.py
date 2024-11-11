from django.shortcuts import render
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
import random

class D3ChartView(LoginRequiredMixin, APIView):
    def get(self, request, *args, **kwargs):
        return render(request, 'charts/chart.html')

class D3ChartDataAPI(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        data = {
            "labels": ["January", "February", "March", "April", "May", "June"],
            "values": [random.randint(10, 100) for _ in range(6)]
        }
        return Response(data)
