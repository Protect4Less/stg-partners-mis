from django.urls import path

from . import views

app_name = 'sales'

urlpatterns = [
    path('', views.statistics, name='statistics'),
    path('', views.monthly_summary, name='monthly-summary'),
    
]