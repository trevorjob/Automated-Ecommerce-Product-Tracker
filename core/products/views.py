from accounts.serializers import RetrieveProductsSerializer
from django.shortcuts import get_object_or_404, render
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from utilities.jumia_scrape import scrape_jumia

from .models import Product
from .serializers import GetOneProductSerializer
from .tasks import test_task

# from rest_framework.permissions
# Create your views here.


class GetProductsView(APIView):
    serializer_class = GetOneProductSerializer
    def post(self, request: Request):
        # data = scrape_jumia("laptops", "80000", "40")
        product = self.serializer_class(name=request.data.get('name'))
        product.save()
        check = test_task.delay(request.data.get('name'))
        
        print(check)
        return Response(data={"data": "data"}, status=status.HTTP_200_OK)


class ListAllProductsView(APIView):
    serializer_class = RetrieveProductsSerializer

    def get(self, request: Request):
        serializer = self.serializer_class(request.user)
        return Response({"data": serializer.data})


class GetOneProductView(APIView):

    queryset = Product.objects.all()
    serializer_class = GetOneProductSerializer

    def get(self, request: Request, product_name: str):
        product_info = get_object_or_404(Product, name=product_name)

        serializer = self.serializer_class(product_info)
        return Response({"data": serializer.data}, status=status.HTTP_200_OK)
