from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from shop.models import Category, Product
from shop.serializers import CategorySerializer, ProductSerializer


class CategoryAPIView(APIView):
    def get(self, *args, **kwargs):
        category = Category.objects.all()
        serializer = CategorySerializer(category, many=True)
        return Response(serializer.data)


class ProductAPIView(ModelViewSet):
    # def get(self, *args, **kwargs):
        # product = Product.objects.all()
        # serializer = ProductSerializer(product, many=True)
        # return Response(serializer.data)
    serializer_class = ProductSerializer
    def get_queryset(self):
        queryset = Product.objects.filter(active=True)
        category_id = self.request.GET.get('category_id')
        if category_id is not None:
            queryset = queryset.filter(category_id = category_id)
        return queryset


class CategoryViewset(ReadOnlyModelViewSet):
    serializer_class = CategorySerializer

    def get_queryset(self):
        return Category.objects.all()
