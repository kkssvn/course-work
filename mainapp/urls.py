"""furniture_shop URL Configuration

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
from django.urls import path

import mainapp.views as mainapp

app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.index, name='index'),

    path('delivery', mainapp.delivery, name='delivery'),

    path('catalog/hits', mainapp.catalog_hits, name='catalog_hits'),


    path('catalog/case', mainapp.catalog_case, name='catalog'),

    path('catalog/kitchen', mainapp.catalog_kitchen, name='catalog_kitchen'),

    path('catalog/wall', mainapp.catalog_wall_furniture, name='catalog_wall_furniture'),

    path('catalog/hallway', mainapp.catalog_hallway, name='catalog_hallway'),

    path('catalog/sofa', mainapp.catalog_sofa, name='catalog_sofa'),

    path('catalog/table', mainapp.catalog_table, name='catalog_table'),

    path('favorite/', mainapp.favorite, name='favorite'),
    path('favorite/add/<int:pk>', mainapp.add_favorite, name='add_favorite'),
    path('favorite/remove/<int:pk>', mainapp.remove_favorite, name='remove_favorite'),
]
