"""
URL configuration for Kebab project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django.contrib import admin
from shayrma import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
path('admin/', admin.site.urls),
path('', views.index, name='home'),
path('kebab/', views.kebab, name='kebab'),
path('Mini_kebab/', views.Mini_kebab, name='Mini_kebab'),
path('potatos/', views.potatos, name='potatos'),
path('drink/', views.drink, name='drink'),
path('kebab_sos/', views.kebab_sos, name='kebab_sos'),
path('card/', views.card, name='card'),
path('pred_card/<int:kebab_url>/', views.pred_card, name='pred_card'),
path('order/', views.order, name='order'),
path('end/', views.end, name='end'),
path('config/', views.config, name='config'),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
