
from django.contrib import admin
from django.urls import path, includeqqq

urlpatterns = [
    path('membership/', include('membership.urls')),
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('auth/', include('django.contrib.auth.urls')),
    path('auth/signup', views.SignUp.as_view(), name='signup'),
    path('auth/settings', views.settings, name='settings'),
    path('join', views.join, name='join'),
    path('checkout', views.checkout, name='checkout'),
    path('success', views.success, name='success'),
    path('cancel', views.cancel, name='cancel'),


]