from django.db import models


# class Villa(models.Model):
#     title = models.CharField(max_length=100, null=True, blank=True, verbose_name='Название виллы')
#     description = models.TextField(null=True, blank=True, verbose_name='Описание виллы')
#     image = models.FileField(null=True, blank=True, verbose_name='Изображение виллы', upload_to='villas')
#
#     def __str__(self):
#         return self.title
#
#     class Meta:
#         verbose_name = 'Вилла'
#         verbose_name_plural = 'Виллы'


class Block(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True, verbose_name='Название блока')
    description = models.TextField(null=True, blank=True, verbose_name='Описание блока')
    floor = models.IntegerField(verbose_name='Количество этажей', null=True, blank=True)
    image = models.FileField(null=True, blank=True, verbose_name='Изображение блока', upload_to='blocks')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Блок'
        verbose_name_plural = 'Блоки'


class Floor(models.Model):
    number = models.IntegerField(null=True, blank=True, verbose_name='Номер этажа')
    block = models.ForeignKey(Block, on_delete=models.CASCADE, verbose_name='Блок', related_name='floors')
    image = models.FileField(null=True, blank=True, verbose_name='Изображение этажа', upload_to='floors')

    def __str__(self):
        return f'Блок-{self.block}, Этаж: {self.number}'

    class Meta:
        verbose_name = 'Этаж'
        verbose_name_plural = 'Этажи'


class Apartment(models.Model):
    floor = models.ForeignKey(Floor, on_delete=models.CASCADE, verbose_name='Этаж', related_name='apartments')
    number = models.IntegerField(null=True, blank=True, verbose_name='Номер апартамента')
    description = models.TextField(null=True, blank=True, verbose_name='Описание апартамента')
    image = models.FileField(null=True, blank=True, verbose_name='Изображение апартамента', upload_to='apartments')
    is_sold = models.BooleanField(default=False, verbose_name='Продано')
    sold_time = models.DateTimeField(null=True, blank=True, verbose_name='Время продажи')
    square = models.FloatField(null=True, blank=True, verbose_name='Площадь')
    price = models.FloatField(null=True, blank=True, verbose_name='Цена')
    rooms = models.IntegerField(null=True, blank=True, verbose_name='Количество комнат')
    pdf_file = models.FileField(null=True, blank=True, verbose_name='PDF файл', upload_to='apartments')

    def __str__(self):
        return f'{self.number}'

    class Meta:
        verbose_name = 'Апартамент'
        verbose_name_plural = 'Апартаменты'


class ApartmentImage(models.Model):
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Апартамент', related_name='images')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение апартамента', upload_to='apartments/images')

    def __str__(self):
        return f'{self.apartment.number}'

    class Meta:
        verbose_name = 'Изображение апартамента'
        verbose_name_plural = 'Изображения апартаментов'
