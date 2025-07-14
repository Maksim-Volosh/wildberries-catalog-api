from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from core.exceptions import NotFoundByQuery, QueryIsRequired
from products.di.container import ProductContainer
from products.serializers import ParseProductInputSerializer

container = ProductContainer()

class ParseProductsAPIView(APIView):
    throttle_scope = 'parse_products'
    
    def post(self, request):
        
        serializer = ParseProductInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        query: str = serializer.validated_data["query"] # type: ignore
        pages: int = serializer.validated_data["pages"] # type: ignore
        
        use_case = container.get_parse_products_use_case()
        
        try:
            use_case.execute(query, pages)
        except QueryIsRequired:
            return Response({'error': "'query' parameter is required"}, status=status.HTTP_400_BAD_REQUEST)
        except NotFoundByQuery:
            return Response({'error': 'Products not found by query'}, status=status.HTTP_404_NOT_FOUND)
        
        return Response({'message': 'Products parsed and created successfully'}, status=status.HTTP_201_CREATED)


class ProductListAPIView(APIView):
    throttle_scope = 'products'
    
    def get(self, request):
        use_case = container.get_filter_products_use_case()
        
        params_parser = container.get_extract_allowed_filters()
        filtered_params = params_parser(request)
        
        data = use_case.execute(filtered_params)
        if not data:
            return Response({'error': 'Products not found'}, status=status.HTTP_404_NOT_FOUND)
        return Response(data)