from django.urls import path

from policy import views
from django.contrib.auth.decorators import login_required

app_name = 'policy'

urlpatterns = [
    path('initiate', views.initiate, name='initiate'),
    path('initiate_policy_lebanon', login_required(views.InitiatePolicyLebanon.as_view()), name='initiate_policy_lebanon'),
    path('listings', views.listings, name='listings'),
    path('bulk-upload', views.bulk_upload, name='bulk-upload'),    
    path('brand-model', views.get_brand_model_ajax, name='brand-model'),
    path('get-model', views.get_model_ajax, name='get-model'),
    path('get-plan-price', views.get_plan_price_ajax, name='get-plan-price'),
    path('get-cat-name-id', views.cat_name_id_ajax, name='get-cat-name-id'),
    path('download_report', views.download_report, name='download_report'),
]
