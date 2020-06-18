from rest_framework import serializers
from products.models import (Category, Product, Menu, Establishment,
                             PaymentType, Review, Kitchen)


class MenuNameField(serializers.Field):

    def to_representation(self, value):
        return value.menu.name

    def to_internal_value(self, data):
        print(data)
        return data


class EstablishmentField(serializers.Field):

    def to_representation(self, value):
        return {
            'name': value.establishment.name,
            'slug': value.establishment.slug
        }

    def to_internal_value(self, data):
        return data


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class KitchenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kitchen
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    establishment = EstablishmentField(source='*')
    menu_name = MenuNameField(source='*')

    class Meta:
        model = Product
        fields = '__all__'


class EstablishmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Establishment
        fields = '__all__'


class PaymentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentType
        fields = '__all__'


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
