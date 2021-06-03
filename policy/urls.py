from django.urls import path

from . import views

app_name = 'policy'

urlpatterns = [
    path('initiate', views.initiate, name='initiate'),
    path('listings', views.listings, name='listings'),
]