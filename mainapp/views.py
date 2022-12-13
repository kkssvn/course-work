from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from mainapp.models import News, Favorite, CatalogCase, CatalogKitchen, CatalogWallFurniture, CatalogHallway, \
    CatalogTable, CatalogSofa


def index(request):
    news = News.objects.all()
    context = {
        'news': news,
    }
    return render(request, 'mainapp/index.html', context)


def catalog_hits(request):
    news = News.objects.all()
    paginate = Paginator(news, 1)
    print(paginate)
    page_number = request.GET.get('page')
    page_object = paginate.get_page(page_number)
    context = {
        'news': news,
    }
    return render(request, 'mainapp/catalog_hits.html', context)


def catalog_case(request):
    catalogs = CatalogCase.objects.all()
    paginate = Paginator(catalogs, 11)
    print(paginate)
    page_number = request.GET.get('page')
    page_object = paginate.get_page(page_number)
    context = {
        'catalogs': page_object,
    }
    return render(request, 'mainapp/catalog_case.html', context)



def catalog_kitchen(request):
    catalog_kitchens = CatalogKitchen.objects.all()
    paginate = Paginator(catalog_kitchens, 11)
    print(paginate)
    page_number = request.GET.get('page')
    page_object = paginate.get_page(page_number)
    context = {
        'catalog_kitchens': page_object,
    }
    return render(request, 'mainapp/catalog_kitchen.html', context)


def catalog_wall_furniture(request):
    catalog_wall = CatalogWallFurniture.objects.all()
    paginate = Paginator(catalog_wall, 11)
    print(paginate)
    page_number = request.GET.get('page')
    page_object = paginate.get_page(page_number)
    context = {
        'catalog_wall': page_object,

    }
    return render(request, 'mainapp/catalog_wall_furniture.html', context)


def catalog_hallway(request):
    catalog_hallways = CatalogHallway.objects.all()
    paginate = Paginator(catalog_hallways, 11)
    print(paginate)
    page_number = request.GET.get('page')
    page_object = paginate.get_page(page_number)
    context = {
        'catalog_hallways': page_object,
    }
    return render(request, 'mainapp/catalog_hallways.html', context)


def catalog_sofa(request):
    catalog_sofas = CatalogSofa.objects.all()
    paginate = Paginator(catalog_sofas, 11)
    print(paginate)
    page_number = request.GET.get('page')
    page_object = paginate.get_page(page_number)
    context = {
        'catalog_sofas': page_object,
    }
    return render(request, 'mainapp/catalog_sofa.html', context)


def catalog_table(request):
    catalog_tables = CatalogTable.objects.all()
    paginate = Paginator(catalog_tables, 11)
    print(paginate)
    page_number = request.GET.get('page')
    page_object = paginate.get_page(page_number)
    context = {
        'catalog_tables': page_object,
    }
    return render(request, 'mainapp/catalog_table.html', context)


def delivery(request):
    deliver = News.objects.all()
    context = {
        'deliver': deliver,
    }
    return render(request, 'mainapp/delivery.html', context)


def favorite(request):
    favor = Favorite.objects.filter(user=request.user)
    context = {
        'title': 'избранное',
        'favorite': favor,
    }
    return render(request, 'mainapp/favorite.html', context)


def add_favorite(request, pk):
    news = get_object_or_404(News, id=pk)

    Favorite.objects.get_or_create(
        news=news,
        user=request.user
    )
    return HttpResponseRedirect(reverse('mainapp:index'))


def remove_favorite(request, pk):
    favor = get_object_or_404(Favorite, id=pk)
    favor.delete()
    return HttpResponseRedirect(reverse('mainapp:favorite'))
