# chat/service/chat_service.py

from llm.service.llm_service import LLMService

class ChatService:
    def __init__(self):
        self.llm = LLMService()

    def ask_with_llm(self, query, companies, categories):
        # llm_service는 top_k 인자를 받지 않음 → 제거
        return self.llm.generate_answer_with_filtering(
            question=query,
            companies=companies,
            categories=categories
        )
