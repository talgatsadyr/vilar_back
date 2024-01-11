from django.contrib import admin

from villa.models import Villa, Block, Floor, Apartment


@admin.register(Villa)
class VillaAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = list_display


@admin.register(Block)
class BlockAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = list_display


@admin.register(Floor)
class FloorAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = list_display


@admin.register(Apartment)
class ApartmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = list_display

# Register your models here.
