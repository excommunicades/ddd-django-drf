from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from apps.auths.domain.value_objects import Email, Password

from apps.auths.domain.entities import UserEntity

class UserRepository:

    @staticmethod
    def create_user(user_entity: UserEntity) -> UserEntity:

        user = User.objects.create_user(
            username = user_entity.username,
            email = user_entity.email.email,
            password = user_entity.password.password,
        )

        return UserEntity(
                    username=user.username,
                    email=Email(email=user.email),
                    password=Password(password=user_entity.password.password))

    @staticmethod
    def check_db_user(user_entity: UserEntity) -> UserEntity:

        if User.objects.filter(email=user_entity.email).first():
            raise ValueError(f'User with this email already exist.')
        return user_entity