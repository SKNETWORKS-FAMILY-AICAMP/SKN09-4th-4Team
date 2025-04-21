# import uuid
# from chat.repository.user_repository import UserRepository
# from chat.entity.user import User


# class UserService:
#     @staticmethod
#     def register_user(user_id: str) -> bool:
#         if UserRepository.exists(user_id):
#             return False  # 이미 존재하는 user_id
#         user = User(user_id=user_id)
#         UserRepository.save(user)
#         return True

# class UserService:
#     @staticmethod
#     def generate_unique_user_id() -> str:
#         while True:
#             user_id = str(uuid.uuid4())
#             if not UserRepository.exists(user_id):
#                 return user_id

#     @staticmethod
#     def get_or_create_user(session) -> str:
#         user_id = session.get('user_id')
#         if user_id and UserRepository.exists(user_id):
#             return user_id
#         # 새로 생성
#         user_id = UserService.generate_unique_user_id()
#         user = User(user_id=user_id)
#         UserRepository.save(user)
#         session['user_id'] = user_id  # 세션에 저장
#         return user_id

# chat/service/user_service.py

import uuid
from chat.repository.user_repository import UserRepository
from chat.models import User  # ✅ Django 모델만 사용

class UserService:
    @staticmethod
    def generate_unique_user_id() -> str:
        while True:
            user_id = str(uuid.uuid4())
            if not UserRepository.exists(user_id):
                return user_id

    @staticmethod
    def get_or_create_user(session) -> str:
        user_id = session.get('user_id')
        if user_id and UserRepository.exists(user_id):
            return user_id
        # 새로 생성
        user_id = UserService.generate_unique_user_id()
        User.objects.create(user_id=user_id)
        session['user_id'] = user_id
        return user_id

    @staticmethod
    def register_user(user_id: str) -> bool:
        if UserRepository.exists(user_id):
            return False
        User.objects.create(user_id=user_id)
        return True
