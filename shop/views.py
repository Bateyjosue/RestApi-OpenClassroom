from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from shop.models import Category, Product
from shop.serializers import CategorySerializer, ProductSerializer

class CategoryAPIView(APIView):
    def get(self, *args, **kwargs):
        category = Category.objects.all()
        serializer = CategorySerializer(category, many=True)
        return Response(serializer.data)

class ProductAPIView(APIView):
    def get(self, *args, **kwargs):
        product = Product.objects.all()
        serializer = ProductSerializer(product, many=True)
        return Response(serializer.data)
    
class CategoryViewset(ModelViewSet):
    serializer_class = CategorySerializer
    
    def get_queryset(self):
        return Category.objects.all()