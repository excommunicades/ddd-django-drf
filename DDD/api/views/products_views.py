from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from api.serializers.products_serializers import ProductSerializer
from products.domain.services import ProductsService
#TODO: Full CRUD for products 
#TODO: Validation for crud owner to products
#TODO: Write tests for products
#TODO: Think about pydantic value objects by serializer



class ProductAPIView(generics.GenericAPIView):

    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request):

        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(status=status.HTTP_201_CREATED, data={"message": "Created successfully!"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs  ):

        product_id = self.kwargs.get('product_id')
        
        if product_id:

            try:
                product = ProductsService.get_product_by_id(product_id)

            except Exception as e:
                return Response({"erorrs": str(e)}, status=status.HTTP_404_NOT_FOUND)

            return Response(status=status.HTTP_200_OK, data=product)
        return Response(status=status.HTTP_200_OK, data=ProductsService.get_product_list())
