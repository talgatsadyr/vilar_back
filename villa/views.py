from django.shortcuts import render
from django.views.generic import TemplateView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny

from villa.models import Villa, Block, Floor, Apartment
from villa.serializers import ApartmentSerializer, VillaSerializer, BlockSerializer, FloorSerializer


class VillaList(ListAPIView):
    serializer_class = VillaSerializer
    queryset = Villa.objects.all()
    permission_classes = [AllowAny]


class BlockList(ListAPIView):
    serializer_class = BlockSerializer
    queryset = Block.objects.all()
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['villa']


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


class TemplateViewIndex(TemplateView):
    template_name = '/oracle_digital/sapat_cargo/cargo/templates/index.html'

