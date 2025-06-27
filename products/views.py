from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from parsers import wildberries_parser
from products.exceptions import NotFoundByQuery, QueryIsRequired
from products.infrastructure import DjangoCache, ORMProductRepository
from products.use_cases import GetFilteredProductsUseCase, ProductParserUseCase


class ParseProductsView(APIView):
    def post(self, request):
        use_case = ProductParserUseCase(
            parser=wildberries_parser,
            repo=ORMProductRepository()
        )
        
        query = request.query_params.get("query")
        pages = request.query_params.get("pages", 1)
        try:
            use_case.execute(query, pages)
        except QueryIsRequired:
            return Response({'error': "'query' parameter is required"}, status=status.HTTP_400_BAD_REQUEST)
        except NotFoundByQuery:
            return Response({'error': 'Products not found by query'}, status=status.HTTP_404_NOT_FOUND)
        
        return Response({'message': 'Products parsed and created successfully'}, status=status.HTTP_201_CREATED)


class ProductListAPIView(APIView):
    def get(self, request):
        use_case = GetFilteredProductsUseCase(
            repo=ORMProductRepository(),
            cache=DjangoCache(),
        )
        data = use_case.execute(request)
        if not data:
            return Response({'error': 'Products not found'}, status=status.HTTP_404_NOT_FOUND)
        return Response(data)