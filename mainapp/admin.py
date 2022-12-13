from django.contrib import admin

from mainapp.models import News, Favorite, CatalogCase, CatalogKitchen, CatalogWallFurniture, \
    CatalogHallway, CatalogSofa, CatalogTable

admin.site.register(News)
admin.site.register(Favorite)
admin.site.register(CatalogCase)
admin.site.register(CatalogKitchen)
admin.site.register(CatalogWallFurniture)
admin.site.register(CatalogHallway)
admin.site.register(CatalogSofa)
admin.site.register(CatalogTable)