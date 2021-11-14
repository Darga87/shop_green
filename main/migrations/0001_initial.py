# Generated by Django 3.2.9 on 2021-11-13 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Наименование')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='e-mail')),
                ('playlist', models.URLField(verbose_name='ссылка на плей лист')),
                ('qty', models.PositiveIntegerField(default=1000)),
                ('comment', models.TextField(verbose_name='коментарий')),
                ('price', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Цена')),
                ('final_price', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Общая цена')),
                ('time_create', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
            },
        ),
    ]
