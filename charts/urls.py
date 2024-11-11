from django.urls import path
from .views import D3ChartView, D3ChartDataAPI

urlpatterns = [
    path('chart/', D3ChartView.as_view(), name='chart'),
    path('api/chart-data/', D3ChartDataAPI.as_view(), name='chart-data'),
]
