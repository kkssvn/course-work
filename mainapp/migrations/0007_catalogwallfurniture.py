# Generated by Django 3.2 on 2022-11-26 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0006_catalogkitchen'),
    ]

    operations = [
        migrations.CreateModel(
            name='CatalogWallFurniture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='', verbose_name='Изображение')),
                ('title', models.CharField(max_length=10, verbose_name='Цена')),
                ('content', models.TextField(verbose_name='Название')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Каталог - гостинная',
                'verbose_name_plural': 'Каталоги - гостинные',
                'ordering': ['-created_at'],
            },
        ),
    ]
