# llm/model/reranker.py

from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import numpy as np

class Reranker:
    def __init__(self, model_name: str = "BAAI/bge-reranker-v2-m3", device: str = None, debug: bool = False):
        self.device = device or ("cuda" if torch.cuda.is_available() else "cpu")
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForSequenceClassification.from_pretrained(model_name).to(self.device)
        self.model.eval()
        self.debug = debug

    def rerank(self, query: str, docs: list[str], top_k: int = 5):
        """
        query: 질문 문자열
        docs: 후보 문장 리스트
        top_k: 상위 몇 개 문서 선택할지
        return: top_k 문장 리스트 (score 포함 가능)
        """

        # 1. (query, doc) 쌍으로 토크나이즈
        pairs = [[query, doc] for doc in docs]
        inputs = self.tokenizer(pairs, return_tensors='pt', padding=True, truncation=True, max_length=512)
        inputs = {k: v.to(self.device) for k, v in inputs.items()}

        # 2. 모델 추론 (score 추출)
        with torch.no_grad():
            outputs = self.model(**inputs)
            scores = outputs.logits.squeeze(-1)  # shape: (N,)

        # 3. score 높은 순으로 정렬
        scores = scores.cpu().numpy()
        scored_docs = list(zip(docs, scores))
        scored_docs.sort(key=lambda x: x[1], reverse=True)

        if self.debug:
            print("\n[BAAI Reranker 결과]")
            for i, (doc, score) in enumerate(scored_docs[:top_k], 1):
                print(f"{i}. Score: {score:.4f}")
                print(f"   문장: {doc[:80]}...\n")

        return [doc for doc, _ in scored_docs[:top_k]]
