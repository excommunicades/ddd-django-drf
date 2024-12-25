from rest_framework import generics, status
from rest_framework.response import Response

from apps.auths.domain.services import UserService
from apps.api.serializers.auth_serializers import UserSerializer

class RegisterUser(generics.GenericAPIView):

    serializer_class = UserSerializer

    def post(self, request):

        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():

            try:

                user_entity = serializer.save()

                return Response({
                    "message": "User created successfully!"
                }, status=status.HTTP_201_CREATED)

            except ValueError as e:

                return Response({
                    "error": str(e)
                }, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
