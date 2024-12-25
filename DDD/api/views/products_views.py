from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from api.serializers.products_serializers import ProductSerializer

#TODO: Full CRUD for products 
#TODO: Write tests for products
#TODO: Think about pydantic value objects by serializer



class CreateProduct(generics.GenericAPIView):

    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request):

        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():

            serializer.save()

            return Response(status=status.HTTP_201_CREATED, data={"message": "Created successfully!"})

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)