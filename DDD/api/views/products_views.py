from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from api.serializers.products_serializers import ProductSerializer
from products.domain.services import ProductsService


class ProductAPIView(generics.GenericAPIView):

    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):

        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():

            product_entity = ProductsService.create_product(
                owner=self.request.user,
                title=serializer.validated_data['title'],
                description=serializer.validated_data.get('description', None),
            )
            return Response(status=status.HTTP_201_CREATED, data=
                                                                {
                                                                    'title': product_entity.title.title,
                                                                    'description': product_entity.description.description
                                                                })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):

        product_id = self.kwargs.get('product_id')
        
        if product_id:

            try:
                product = ProductsService.get_product_by_id(product_id)

            except Exception as e:
                return Response({"erorrs": str(e)}, status=status.HTTP_404_NOT_FOUND)

            return Response(status=status.HTTP_200_OK, data=product)
        return Response(status=status.HTTP_200_OK, data=ProductsService.get_product_list())

    def patch(self, request, *args, **kwargs):

        serializer = self.get_serializer(data=request.data)
        product_id = self.kwargs.get('product_id')

        if serializer.is_valid():

            try:

                product_entity = ProductsService.udpate_product(
                    id=int(product_id),
                    owner=self.request.user,
                    title=serializer.validated_data['title'],
                    description=serializer.validated_data.get('description', None),
                )

            except Exception as e:

                if str(e) == 'You must to be an owner of this product for update operation.':
                    return Response({"erorrs": str(e)}, status=status.HTTP_400_BAD_REQUEST)

                return Response({"erorrs": str(e)}, status=status.HTTP_404_NOT_FOUND)

            return Response(status=status.HTTP_200_OK, data=
                                                            {
                                                                'title': product_entity.title,
                                                                'description': product_entity.description
                                                            })

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):

        product_id = self.kwargs.get('product_id')

        try:
            product_entity = ProductsService.delete_product(id=int(product_id), request_user_id=int(self.request.user.id))

        except Exception as e:

            if str(e) == 'You must to be an owner of this product for update operation.':
                return Response({"erorrs": str(e)}, status=status.HTTP_400_BAD_REQUEST)

            return Response({"erorrs": str(e)}, status=status.HTTP_404_NOT_FOUND)

        return Response(status=status.HTTP_204_NO_CONTENT, data={"message": f"Product with id: {int(product_id)} was deleted successfully!"})
