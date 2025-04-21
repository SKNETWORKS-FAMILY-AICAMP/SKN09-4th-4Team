# llm_service.py
from llm.model.generator import Generator
from llm.service.search_service import SearchService

class LLMService:
    def __init__(self):
        self.generator = Generator("CarrotAI/Llama-3.2-Rabbit-Ko-3B-Instruct")
        self.search_service = SearchService()

    def generate_answer_with_filtering(self, question, companies, categories):
        context_docs = self.search_service.search_with_rerank(question, companies, categories)

        if not context_docs:
            return "죄송합니다. 관련 문서를 찾을 수 없습니다."

        context = "\n".join([doc['text'] for doc in context_docs])
        prompt = self._build_prompt(context, question)
        print("\n[📥 LLM 입력 프롬프트]")
        print(prompt[:300])  # 너무 길면 300자까지만

        answer = self.generator.generate(prompt)
        print("\n[🤖 LLM 생성 응답]")
        print(answer)
        return answer

    def _build_prompt(self, context, question):
        return f"[문서 시작]\n{context}\n[문서 끝]\n\n[질문]\n{question}\n\n[답변]"
