from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import status

from django_filters.rest_framework import DjangoFilterBackend

from products.exceptions import QueryIsRequired, NotFoundByQuery
from products.infrastructure import ORMProductRepository
from products.models import Product
from products.serializers import ProductSerializer
from products.use_cases import ProductParserUseCase
from products.filters import ProductFilter


from parsers import wildberries_parser

class ParseProductsView(APIView):
    def post(self, request):
        product_parser = ProductParserUseCase(parser=wildberries_parser, repo=ORMProductRepository())
        
        try:
            product_parser.execute(request)
        except QueryIsRequired:
            return Response({'error': 'Query param is required'}, status=status.HTTP_400_BAD_REQUEST)
        except NotFoundByQuery:
            return Response({'error': 'Products not found by query'}, status=status.HTTP_404_NOT_FOUND)
        
        return Response({'message': 'Products parsed and created successfully'}, status=status.HTTP_201_CREATED)


class ProductListAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductFilter
