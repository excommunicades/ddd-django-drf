from .aggregates import UserAggregate
from .value_objects import Email, Password
from apps.auths.db.repositories import UserRepository
from apps.auths.domain.entities import UserEntity

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
