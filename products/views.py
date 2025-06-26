from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from parsers import wildberries_parser

from products.services.create_parsed import CreateParsedProducts

class ProductsView(APIView):
    def post(self, request):
        query = request.query_params.get("query")
        pages = request.query_params.get("pages", 1)
        if not query:
            return Response({'error': 'Query and pages are required'}, status=status.HTTP_400_BAD_REQUEST)
        create_parsed_products = CreateParsedProducts(parser=wildberries_parser)
        create_parsed_products.create(query=query, pages=int(pages))
        
        return Response({'message': 'Product created successfully'}, status=status.HTTP_201_CREATED)
