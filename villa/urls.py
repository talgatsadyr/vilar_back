from django.contrib import admin
from django.urls import path

from villa.views import VillaList, BlockList, FloorList, ApartmentList

urlpatterns = [
    path('villa_list/', VillaList.as_view(), name='villa_list'),
    path('block_list/', BlockList.as_view(), name='block_list'),
    path('floor_list/', FloorList.as_view(), name='floor_list'),
    path('apartment_list/', ApartmentList.as_view(), name='apartment_list'),
]