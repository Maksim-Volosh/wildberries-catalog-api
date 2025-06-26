from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from products.exceptions import QueryIsRequired  
from products.infrastructure import ORMProductRepository
from products.use_cases import ProductParserUseCase

from parsers import wildberries_parser

class ProductsView(APIView):
    def post(self, request):
        product_parser = ProductParserUseCase(parser=wildberries_parser, repo=ORMProductRepository())
        
        try:
            product_parser.execute(request)
        except QueryIsRequired:
            return Response({'error': 'Query param is required'}, status=status.HTTP_400_BAD_REQUEST)
        
        return Response({'message': 'Products parsed and created successfully'}, status=status.HTTP_201_CREATED)
