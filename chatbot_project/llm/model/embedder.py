import torch
from transformers import AutoTokenizer, AutoModel
from typing import Optional

class Embedder:
    def __init__(self, model_name: str, device: Optional[str] = None):
        """
        model_name: 사용할 임베딩 모델 이름
        device: 'cpu' 또는 'cuda'. 생략하면 자동 선택
        """
        self.device = device or ("cuda" if torch.cuda.is_available() else "cpu")
        self.tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
        self.model = AutoModel.from_pretrained(model_name, trust_remote_code=True).to(self.device)
        self.model.eval()
        self.model_name = model_name

    def get_embedding(self, text: str) -> torch.Tensor:
        inputs = self.tokenizer(text, return_tensors="pt", truncation=True, padding=True, max_length=512)
        inputs = {k: v.to(self.device) for k, v in inputs.items()}

        # pool_mask는 카카오 embedding 모델 기준
        if "pool_mask" in self.model.forward.__code__.co_varnames:
            inputs["pool_mask"] = inputs["attention_mask"]

        with torch.no_grad():
            outputs = self.model(**inputs)

        # 모델에 따라 반환 형식이 다를 수 있음
        # kakaocorp/kanana-nano: outputs["embedding"]
        # 일반 BERT 기반 모델: outputs.last_hidden_state.mean(dim=1)
        if "embedding" in outputs:
            return outputs["embedding"].cpu().numpy().astype("float32")
        else:
            return outputs.last_hidden_state.mean(dim=1).cpu().numpy().astype("float32")
