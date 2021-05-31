from django.urls import path

from . import views

app_name = 'policy'

urlpatterns = [
    path('initiate/<int:partner_code>', views.initiate, name='initiate'),
]