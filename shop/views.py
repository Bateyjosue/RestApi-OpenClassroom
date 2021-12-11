from rest_framework.views import APIView
from rest_framework.response import Response

from shop.models import Category
from shop.serializers import CategorySerializer

class CategoryAPIView(APIView):
    def get(self, *args, **kwargs):
        category = Category.objects.all()
        serializer = CategorySerializer(category, many=True)
        return Response(serializer.data)