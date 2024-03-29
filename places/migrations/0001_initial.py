# Generated by Django 3.2.23 on 2024-01-16 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название')),
                ('description_short', models.CharField(max_length=250, verbose_name='Краткое описание')),
                ('description_long', models.TextField(verbose_name='Большое описание')),
                ('long', models.DecimalField(decimal_places=14, max_digits=17, verbose_name='Долгота')),
                ('lat', models.DecimalField(decimal_places=14, max_digits=17, verbose_name='Широта')),
            ],
        ),
    ]
