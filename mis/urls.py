from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView
# from django.contrib import admin
from django.urls import include,path,re_path

urlpatterns = [
	re_path('', include('dashboard.urls')),
	re_path('sales/', include('sales.urls')),
	re_path('pages/', include('pages.urls')),
    re_path('login/', LoginView.as_view(), name='login'),
	re_path('policy/', include('policy.urls')),

]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)