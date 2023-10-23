from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet

router = DefaultRouter()
router.register(r"products", ProductViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path(
        "find_products_in_category",
        ProductViewSet.as_view({"get": "find_products_in_category"}),
    ),
]


