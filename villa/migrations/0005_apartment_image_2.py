# Generated by Django 5.0.1 on 2024-01-12 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('villa', '0004_apartment_pdf_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='apartment',
            name='image_2',
            field=models.FileField(blank=True, null=True, upload_to='apartments', verbose_name='Изображение апартамента без мебели'),
        ),
    ]