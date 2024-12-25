from pydantic import ValidationError

from django.contrib.auth.models import User

from .entities import UserEntity
from auths.db.repositories import UserRepository

class UserAggregate:

    def __init__(self, user_entity: UserEntity):

        self.user_entity = user_entity

    @staticmethod
    def create_user(user_entity: UserEntity):

        if len(user_entity.password.password) < 8:
            raise ValueError('Password must be more then 8 characters.')
        try:
            user_entity = UserRepository.check_db_user(user_entity)

        except ValueError as e:
            raise e

        return UserAggregate(user_entity)

    @staticmethod
    def login_user(user_entity: UserEntity):

        try:
            user_entity = UserRepository.login_user_by_email(user_entity)
            return UserAggregate(user_entity)

        except ValueError as e:
            raise e
