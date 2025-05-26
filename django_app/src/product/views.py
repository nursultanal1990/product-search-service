from django.http import JsonResponse
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.status import HTTP_200_OK

from product.services.product_cache import get_or_request_product


class ProductDetailView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_description="Fetch product by key",
        responses={
            200: openapi.Response(description=""),
            400: openapi.Response(description=""),
        },
    )
    def get(self, request, key: str, *args, **kwargs):
        product = get_or_request_product(product_id=key)

        if product:
            return JsonResponse(product, status=HTTP_200_OK)

        return JsonResponse(
            {
                "status": "processing",
                "message": "Product not found in cache. Requested from backend."
            },
            status=202
        )
