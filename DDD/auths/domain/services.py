from rest_framework_simplejwt.tokens import RefreshToken

from .aggregates import UserAggregate
from .value_objects import Email, Password
from auths.db.repositories import UserRepository
from auths.domain.entities import UserEntity

class UserService:

    @staticmethod
    def register_user(username: str, email: str, password: str):

        user_entity = UserEntity(
                        username=username,
                        email=Email(email=email),
                        password=Password(password=password))

        try:
            user_aggregate = UserAggregate.create_user(user_entity)
            return UserRepository.create_user(user_aggregate.user_entity)

        except ValueError as e:
            raise ValueError(str(e))

    @staticmethod
    def login_user(email: str, password: str):

        user_entity = UserEntity(
                        email=Email(email=email),
                        password=Password(password=password))
        try:
            user_aggregate = UserAggregate.login_user(user_entity)
            
            refresh = RefreshToken.for_user(user_aggregate.user_entity)

            return {
                "tokens": {
                    'refresh_token': str(refresh),
                    'access_token': str(refresh.access_token),
                    },
                "user": {
                    "id": user_aggregate.user_entity.id,
                    "username": user_aggregate.user_entity.username,
                    "email": user_aggregate.user_entity.email
                }
            }

        except ValueError as e:
            raise ValueError(str(e))