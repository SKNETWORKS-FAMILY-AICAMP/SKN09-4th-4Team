import os
import json
import pickle
import faiss

def build_vector_db_sources(companies, categories):
    """
    보험사 + 보험종류 조합에 따라 벡터DB 디렉토리 정보를 구성
    예: AXA + car → ./AXA_db/faiss_index_axa_car, metadata_axa_car, file_mapping_axa_car.json
    """
    base_dir = "llm/vector_db"
    sources = []

    for company in companies:
        for category in categories:
            company_key = f"{company.upper()}_db"
            index_dir = os.path.join(base_dir, company_key, f"faiss_index_{company.lower()}_{category}")
            meta_dir = os.path.join(base_dir, company_key, f"metadata_{company.lower()}_{category}")
            mapping_path = os.path.join(base_dir, company_key, f"file_mapping_{company.lower()}_{category}.json")

            if os.path.exists(index_dir) and os.path.exists(meta_dir) and os.path.exists(mapping_path):
                sources.append({
                    "label": company,
                    "category": category,
                    "index_dir": index_dir,
                    "meta_dir": meta_dir,
                    "mapping_path": mapping_path
                })
            # print(os.path.exists(index_dir))
    return sources

def search_all_sources(query, sources, embedder, top_k=5):
    query_vector = embedder.get_embedding(query)
    all_results = []

    for source in sources:
        INDEX_DIR = source["index_dir"]
        META_DIR = source["meta_dir"]
        MAPPING_PATH = source["mapping_path"]
        company = source["label"]
        category = source["category"]

        # 상품명 매핑 로드
        if not os.path.exists(MAPPING_PATH):
            continue
        with open(MAPPING_PATH, "r", encoding="utf-8") as f:
            file_mapping = json.load(f)

        # 폴더 내 모든 상품별 faiss/pkl 검색
        for file in os.listdir(INDEX_DIR):
            if not file.endswith(".faiss"):
                continue

            doc_id = file.replace(".faiss", "")
            faiss_path = os.path.join(INDEX_DIR, file)
            meta_path = os.path.join(META_DIR, f"{doc_id}.pkl")

            if not os.path.exists(faiss_path) or not os.path.exists(meta_path):
                continue

            index = faiss.read_index(faiss_path)
            with open(meta_path, "rb") as f:
                passages = pickle.load(f)

            D, I = index.search(query_vector, top_k * 3)  # 중복 제거를 위해 넉넉히 추출
            for dist, idx in zip(D[0], I[0]):
                if idx < len(passages):
                    text = passages[idx]
                    all_results.append({
                        "text": str(text.page_content if hasattr(text, "page_content") else text),
                        "distance": float(dist),
                        "doc_id": doc_id,
                        "doc_name": file_mapping.get(doc_id, doc_id),
                        "company": company,
                        "category": category
                    })
    print("[🔎 벡터 검색 결과]")
    for r in all_results[:5]:  # 상위 5개만
        print(f"- 거리: {r['distance']:.4f} | 보험사: {r['company']} | 카테고리: {r['category']}")
        print(f"  텍스트: {r['text'][:80]}...\n")
        
    # 중복 제거 + top_k 정렬
    seen = set()
    final_results = []
    for result in sorted(all_results, key=lambda x: x["distance"]):
        norm = " ".join(result["text"].strip().lower().split())
        if norm not in seen:
            seen.add(norm)
            final_results.append(result)
        if len(final_results) >= top_k:
            break

    
    return final_results

