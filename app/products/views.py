from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from products.models import Category, Product, Menu, Establishment, PaymentType, Review, Kitchen
from products.serializers import CategorySerializer, ProductSerializer, \
    EstablishmentSerializer, MenuSerializer, PaymentTypeSerializer, \
    ReviewSerializer, KitchenSerializer
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as filters


class LargeResultsSetPagination(PageNumberPagination):
    page_size = 1000
    page_size_query_param = 'page_size'
    max_page_size = 10000


class ReviewFilter(filters.FilterSet):
    class Meta:
        model = Review
        fields = ['establishment']


class CategoriesViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class KitchenViewSet(viewsets.ModelViewSet):
    queryset = Kitchen.objects.all()
    serializer_class = KitchenSerializer


class ProductsViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = LargeResultsSetPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['establishment__slug', 'promo', 'popular']


class EstablishmentViewSet(viewsets.ModelViewSet):
    serializer_class = EstablishmentSerializer
    queryset = Establishment.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category__slug', 'popular']


class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()
    filter_backends = [DjangoFilterBackend]
    # filter_fields = ['establishment']
    filterset_class = ReviewFilter
    # def get_queryset(self):
    #     slug = self.request.query_params
    #     queryset = Review.objects.filter(establishment__slug=self.kwargs.get('slug'))
    #     return queryset
