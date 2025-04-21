# generator.py

import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

class Generator:
    def __init__(self, model_name: str = "kakaocorp/KoGPT", device: str = None, max_new_tokens: int = 512):
        self.device = device or ("cuda" if torch.cuda.is_available() else "cpu")
        self.tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
        self.model = AutoModelForCausalLM.from_pretrained(model_name, trust_remote_code=True).to(self.device)
        self.model.eval()
        self.max_new_tokens = max_new_tokens

    def generate(self, prompt: str) -> str:
        inputs = self.tokenizer(prompt, return_tensors="pt", truncation=True).to(self.device)
        with torch.no_grad():
            output = self.model.generate(
                **inputs,
                max_new_tokens=self.max_new_tokens,
                pad_token_id=self.tokenizer.eos_token_id,
                do_sample=False,
                top_k=50,
                top_p=0.95
            )
        result = self.tokenizer.decode(output[0], skip_special_tokens=True)

        # [답변] 이후 텍스트만 추출
        if "[답변]" in result:
            return result.split("[답변]")[-1].strip()
        print("답변내용:",result.strip())
        return result.strip()
