from django.shortcuts import render
from django.views.generic import TemplateView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.generics import ListAPIView, GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from villa.models import Block, Floor, Apartment
from villa.serializers import ApartmentSerializer, BlockSerializer, FloorSerializer


class BlockList(ListAPIView):
    serializer_class = BlockSerializer
    queryset = Block.objects.all()
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend]


class FloorList(ListAPIView):
    serializer_class = FloorSerializer
    queryset = Floor.objects.all()
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['block']


class ApartmentList(ListAPIView):
    serializer_class = ApartmentSerializer
    queryset = Apartment.objects.all()
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['floor']


class ApartmentView(GenericAPIView):
    serializer_class = ApartmentSerializer
    permission_classes = [AllowAny]

    def get(self, request, pk):
        apartment = Apartment.objects.get(pk=pk)
        serializer = ApartmentSerializer(apartment)
        return Response(serializer.data, status=status.HTTP_200_OK)
