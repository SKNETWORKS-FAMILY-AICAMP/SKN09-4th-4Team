from llm.service.llm_service import generate_answer
from llm.service.search_service import search_documents

chat_log = []  # 실사용시 DB나 세션에 저장하는 게 좋음

def process_chat(user_input):
    relevant_docs = search_documents(user_input)
    answer = generate_answer(user_input, relevant_docs)

    # 기록 저장
    chat_log.append({'q': user_input, 'a': answer})
    return answer, chat_log
