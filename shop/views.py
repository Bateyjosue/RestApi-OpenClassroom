from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Category
from .serializers import CategorySerializer

class CategoryAPIView(APIView):
    def get_user_model(self, *args, **kwargs):
        category = Category.objects.all()
        serializer = CategorySerializer(category, many=True)
        return Response(serializer.data)