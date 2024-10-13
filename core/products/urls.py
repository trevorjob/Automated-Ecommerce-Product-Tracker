from django.urls import path
from .views import GetProductsView, ListAllProductsView

urlpatterns = [
    path("scrape/", GetProductsView.as_view(), name="scrape_data"),
    path("products/", ListAllProductsView.as_view(), name="get_post_products"),
]
