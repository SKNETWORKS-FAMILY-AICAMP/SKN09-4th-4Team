# from chat.entity.user import User

from chat.models import User  # ✅ UserModel → User 로 변경

class UserRepository:
    @staticmethod
    def save(user: User) -> User:
        obj, created = User.objects.get_or_create(user_id=user.user_id)
        return user

    @staticmethod
    def exists(user_id: str) -> bool:
        return User.objects.filter(user_id=user_id).exists()

