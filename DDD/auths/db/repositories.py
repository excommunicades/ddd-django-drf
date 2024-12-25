from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import authenticate

from auths.domain.value_objects import Email, Password
from auths.domain.entities import UserEntity

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
    def login_user_by_email(user_entity: UserEntity) -> UserEntity:

        try:

            user = User.objects.get(email=str(user_entity.email))

            if not user.check_password(str(user_entity.password)):
                raise ValueError('Wrong password.')

            user_entity = user
            return user_entity

        except Exception as e:
            raise ValueError(str(e))

    @staticmethod
    def check_db_user(user_entity: UserEntity) -> UserEntity:

        if User.objects.filter(email=user_entity.email).first():
            raise ValueError('User with this email already exist.')
        return user_entity