from django.contrib import admin
from django.contrib.auth.models import Group, User
from villa.models import Block, Floor, Apartment, ApartmentImage


# @admin.register(Villa)
# class VillaAdmin(admin.ModelAdmin):
#     list_display = ('id', 'title')
#     list_display_links = list_display

class FloorInline(admin.TabularInline):
    model = Floor
    extra = 1


@admin.register(Block)
class BlockAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = list_display
    inlines = [FloorInline]


@admin.register(Floor)
class FloorAdmin(admin.ModelAdmin):
    list_display = ('id', 'number', 'block')
    list_display_links = list_display


class ApartmentInline(admin.TabularInline):
    model = ApartmentImage
    extra = 1


@admin.register(Apartment)
class ApartmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'number', 'floor', 'is_sold')
    list_display_links = list_display
    search_fields = ('number', 'floor__number', 'floor__block__title')
    list_filter = ('is_sold', 'floor',)
    inlines = [ApartmentInline]



admin.site.unregister(Group)
admin.site.unregister(User)


