# Generated by Django 3.2 on 2022-11-26 19:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_auto_20221126_2350'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Catalog',
            new_name='CatalogCase',
        ),
        migrations.AlterModelOptions(
            name='catalogcase',
            options={'ordering': ['-created_at'], 'verbose_name': 'Каталог - шкаф', 'verbose_name_plural': 'Каталоги - шкафы'},
        ),
    ]
