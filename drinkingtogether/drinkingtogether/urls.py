"""drinkingtogether URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include

from digitalbeercrate import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', views.BeerCrateView.as_view(), name="beercrate_index"),
    path('config', views.ConfigView.as_view(), name="beercrate_config"),
    path('confog/new/', views.ConfigCreate.as_view(), name="beercrate_config_create"),
    path('config/edit/<int:pk>', views.ConfigEdit.as_view(), name="beercrate_config_edit"),
    path('config/delete/<int:pk>', views.ConfigDelete.as_view(), name="beercrate_config_delete"),
    path('beer/add', views.get_beer, name="beercrate_get"),
    path('beer/update', views.update_beer, name="beercrate_update"),
]
