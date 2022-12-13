from django.contrib.auth.models import User
from django.db import models


class News(models.Model):
    image = models.ImageField(verbose_name='Изображение')
    title = models.CharField(verbose_name='Цена', max_length=10)
    content = models.TextField(verbose_name='Название')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Хит'
        verbose_name_plural = 'Хиты'


class CatalogCase(models.Model):
    image = models.ImageField(verbose_name='Изображение')
    title = models.CharField(verbose_name='Цена', max_length=10)
    content = models.TextField(verbose_name='Название')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Каталог - шкаф'
        verbose_name_plural = 'Каталоги - шкафы'


class CatalogKitchen(models.Model):
    image = models.ImageField(verbose_name='Изображение')
    title = models.CharField(verbose_name='Цена', max_length=10)
    content = models.TextField(verbose_name='Название')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Каталог - кухня'
        verbose_name_plural = 'Каталоги - кухни'


class CatalogWallFurniture(models.Model):
    image = models.ImageField(verbose_name='Изображение')
    title = models.CharField(verbose_name='Цена', max_length=10)
    content = models.TextField(verbose_name='Название')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Каталог - гостинная'
        verbose_name_plural = 'Каталоги - гостинные'


class CatalogHallway(models.Model):
    image = models.ImageField(verbose_name='Изображение')
    title = models.CharField(verbose_name='Цена', max_length=10)
    content = models.TextField(verbose_name='Название')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Каталог - шкаф прихожая'
        verbose_name_plural = 'Каталоги - шкафы прихожие'


class CatalogSofa(models.Model):
    image = models.ImageField(verbose_name='Изображение')
    title = models.CharField(verbose_name='Цена', max_length=10)
    content = models.TextField(verbose_name='Название')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Каталог - диван'
        verbose_name_plural = 'Каталоги - диваны'


class CatalogTable(models.Model):
    image = models.ImageField(verbose_name='Изображение')
    title = models.CharField(verbose_name='Цена', max_length=10)
    content = models.TextField(verbose_name='Название')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Каталог - стол'
        verbose_name_plural = 'Каталоги - столы'


class Favorite(models.Model):
    news = models.ForeignKey(News, verbose_name='Новость', on_delete=models.CASCADE)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Избранное'
        verbose_name_plural = 'Избранные'

