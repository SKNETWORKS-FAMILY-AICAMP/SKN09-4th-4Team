# chat/service/feedback_service.py
from chat.models import ChatLog

def save_feedback(user_id, question, answer, feedback, turn):
    chat_id = f"{user_id}-{str(turn).zfill(2)}"
    ChatLog.objects.create(
        chat_id =chat_id ,
        user_id=user_id,
        question=question,
        answer=answer,
        feedback=feedback,
        turn=turn
    )

# from chat.entity.feedback import User
# from chat.repository.feedback_repository import UserRepository

# class UserService:
#     @staticmethod
#     def register_user(user_id: str) -> bool:
#         if UserRepository.exists(user_id):
#             return False  # 이미 존재하는 user_id
#         user = User(user_id=user_id)
#         UserRepository.save(user)
#         return True

