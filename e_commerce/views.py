from rest_framework.response import Response
from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer
from django.core.cache import cache


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def find_products_in_category(self, request):
        """
        Retrieves and serializes products based on a specified category.

        Args:
            request (Request): The HTTP request containing the 'category' parameter.

        Returns:
            Response: Serialized product data in the specified category.
        """
        category = request.data.get("category")
        # Check if the data is cached
        cached_data = cache.get(f"category_{category}_products")
        
        if cached_data is not None:
            # If cached data exists, return it
            return Response(cached_data)
        required_products = Product.objects.filter(category=category)
        serializer = ProductSerializer(required_products, many=True)

        # Cache the data for a specified duration (for 15 min)
        cache.set(f"category_{category}_products", serializer.data, 60*15)
        return Response(serializer.data)
