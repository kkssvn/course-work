# Generated by Django 3.2 on 2022-12-04 06:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0013_delete_mail'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ['-created_at'], 'verbose_name': 'Хит', 'verbose_name_plural': 'Хиты'},
        ),
    ]
