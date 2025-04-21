from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from chat.service.chat_service import ChatService
from chat.models import ChatLog
from django.http import JsonResponse
from chat.service.user_service import UserService
import json
import uuid



def intro_view(request):
    return render(request, "chat/intro.html")

# def chat_view(request):
#     return render(request, "chat/chat.html")


@csrf_exempt
def ask_llm_view(request):
    print(f"[🤖 질문 요청 수신] URL: {request.path} | Method: {request.method}")

    if request.method == 'POST':
        companies = request.POST.getlist('companies')
        categories = request.POST.getlist('categories')
        query = request.POST.get('query')

        # ✅ user_id 먼저 생성
        user_id = UserService.get_or_create_user(request.session)

        chat_service = ChatService()
        answer = chat_service.ask_with_llm(query, companies, categories)

        turn = ChatLog.objects.filter(user_id=user_id).count() + 1
        chat_id = f"{user_id}-{str(turn).zfill(2)}"

        print("[🧠 질문 처리 시작]")
        print("  user_id:", user_id)
        print("  question:", query)
        print("  answer:", answer)
        print("  저장 예정 turn:", turn)

        ChatLog.objects.create(
            chat_id=chat_id,
            user_id=user_id,
            question=query,
            answer=answer,
            turn=turn
        )

        print("[✅ ChatLog 저장 완료]")
        print("  chat_id:", chat_id)
        print("[🧠 응답 반환]", { "answer": answer, "turn": turn })
        return JsonResponse({'answer': answer, 'turn': turn})




# def intro_view(request):
#     user_id = UserService.get_or_create_user(request.session)
#     return render(request, "chat/intro.html", {'user_id': user_id})


def chat_view(request):
    print(f"[🟢 CHAT 페이지 진입] URL: {request.path} | Method: {request.method}")
    user_id = UserService.get_or_create_user(request.session)
    return render(request, "chat/chat.html", {'user_id': user_id})  # ✅ user_id 템플릿으로 전달

@csrf_exempt
def save_chatlog_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            user_id = data.get("user_id")
            question = data.get("question")
            answer = data.get("answer")
            turn = int(data.get("turn"))

            print("[📝 ChatLog 저장 시도]")
            print("  user_id:", user_id)
            print("  turn:", turn)

            chat_id = f"{user_id}-{str(turn).zfill(2)}"

            ChatLog.objects.create(
                chat_id=chat_id,
                user_id=user_id,
                question=question,
                answer=answer,
                turn=turn
            )

            print("[✅ 저장 완료] chat_id:", chat_id)
            return JsonResponse({'status': 'ok'})

        except Exception as e:
            print("[❌ 저장 중 오류]", str(e))
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Invalid method'}, status=405)
