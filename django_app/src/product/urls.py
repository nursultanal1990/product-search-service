from django.urls import path

from .views import ProductDetailView


urlpatterns = [
    path(
        "products/<str:key>",
        ProductDetailView.as_view(),
        name="product-detail",
    ),
]
