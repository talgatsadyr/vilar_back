from django.urls import path
from villa.views import BlockList, FloorList, ApartmentList, ApartmentView, FloorDetail

urlpatterns = [
    path('block_list/', BlockList.as_view(), name='block_list'),
    path('floor_list/', FloorList.as_view(), name='floor_list'),
    path('apartment_list/', ApartmentList.as_view(), name='apartment_list'),
    path('apartment_detail/<int:number>/', ApartmentView.as_view(), name='apartment_detail'),
    path('floor_detail/<int:id>/', FloorDetail.as_view(), name='floor_detail'),
]