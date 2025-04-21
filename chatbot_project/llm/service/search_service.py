# llm/service/search_service.py

from llm.model.embedder import Embedder
from llm.model.reranker import Reranker
from llm.repository.vectordb_repository import build_vector_db_sources, search_all_sources

class SearchService:
    def __init__(
        self,
        embed_model_name: str = "kakaocorp/kanana-nano-2.1b-embedding",
        rerank_model_name: str = "BAAI/bge-reranker-v2-m3",
        debug: bool = True
    ):
        self.embedder = Embedder(embed_model_name)
        self.reranker = Reranker(rerank_model_name, debug=debug)
        self.debug = debug

    def normalize_text(self, text):
        return " ".join(str(text).strip().lower().split())

    def search_with_rerank(self, query: str, companies: list, categories: list, top_k: int = 5) -> list:
        """
        1. 보험사 + 보험종류 조합 → 해당 폴더에서 모든 상품에 대해 벡터 유사도 검색
        2. 결과 문장들을 Reranker로 재정렬
        3. 최종 Top-K 문장 반환
        """
        # Step 1. 벡터 검색
        sources = build_vector_db_sources(companies, categories)
        search_results = search_all_sources(query, sources, self.embedder, top_k=top_k * 3)  # 여유있게 뽑음

        if not search_results:
            return []

        # Step 2. Rerank를 위한 텍스트만 추출
        candidate_texts = [r["text"] for r in search_results]
        reranked_texts = self.reranker.rerank(query, candidate_texts, top_k=top_k)

        # Step 3. reranked_texts 기준으로 원본 결과에서 재정렬
        text_to_result = {self.normalize_text(r["text"]): r for r in search_results}
        final_results = []
        seen = set()
        for text in reranked_texts:
            norm = self.normalize_text(text)
            if norm in text_to_result and norm not in seen:
                final_results.append(text_to_result[norm])
                seen.add(norm)
            if len(final_results) >= top_k:
                break

        if self.debug:
            print("\n[🔍 최종 선택된 문서들]")
            for i, r in enumerate(final_results, 1):
                print(f"{i}. 보험사: {r['company']} | 종류: {r['category']} | 상품명: {r['doc_name']}")
                print(f"   내용: {r['text'][:100]}...\n")

        return final_results
