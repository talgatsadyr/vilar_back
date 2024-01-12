# Generated by Django 5.0.1 on 2024-01-12 12:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('villa', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='block',
            name='villa',
        ),
        migrations.RemoveField(
            model_name='apartment',
            name='title',
        ),
        migrations.RemoveField(
            model_name='floor',
            name='title',
        ),
        migrations.AddField(
            model_name='floor',
            name='number',
            field=models.IntegerField(blank=True, null=True, verbose_name='Номер этажа'),
        ),
        migrations.RemoveField(
            model_name='block',
            name='floor',
        ),
        migrations.AlterField(
            model_name='floor',
            name='block',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='floors', to='villa.block', verbose_name='Блок'),
        ),
        migrations.CreateModel(
            name='ApartmentImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='apartments/images', verbose_name='Изображение апартамента')),
                ('apartment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='villa.apartment', verbose_name='Апартамент')),
            ],
            options={
                'verbose_name': 'Изображение апартамента',
                'verbose_name_plural': 'Изображения апартаментов',
            },
        ),
        migrations.DeleteModel(
            name='Villa',
        ),
        migrations.AddField(
            model_name='block',
            name='floor',
            field=models.IntegerField(blank=True, null=True, verbose_name='Количество этажей'),
        ),
    ]
