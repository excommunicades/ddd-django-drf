from rest_framework import generics, status
from rest_framework.response import Response

from apps.auths.domain.services import UserService
from apps.api.serializers.auth_serializers import (
    UserRegistrationSerializer,
    UserLoginSerializer,
)

class RegisterUser(generics.GenericAPIView):

    serializer_class = UserRegistrationSerializer

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


class LoginUser(generics.GenericAPIView):

    serializer_class = UserLoginSerializer

    def post(self,request):

        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():

            try:

                user = UserService.login_user(serializer.validated_data['email'], serializer.validated_data['password'])

                return Response({"message": "you are loggined"}, status=status.HTTP_200_OK)

            except ValueError as e:

                return Response({"errors": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
