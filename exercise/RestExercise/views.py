
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework_extensions.mixins import NestedViewSetMixin

from .models import Category, Item
from .serializers import ItemSerializer,CategorySerializer
# Create your views here.


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ItemsViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    serializer_class = ItemSerializer
    queryset = Item.objects.all()
