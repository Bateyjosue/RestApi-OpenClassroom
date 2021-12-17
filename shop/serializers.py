from rest_framework.serializers import ModelSerializer
from shop.models import Category, Product

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description','active', 'date_updated', 'date_created']

class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'date_created', 'date_updated', 'name', 'category', 'active' ]