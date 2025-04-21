from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from chat.models import ChatLog
from datetime import datetime

# @csrf_exempt
# def save_feedback_view(request):
#     print(f"[💬 피드백 요청 수신] URL: {request.path} | Method: {request.method}")

#     if request.method == 'POST':
#         try:
#             data = json.loads(request.body)
#             user_id = data.get('user_id')
#             turn_raw = data.get('turn')
#             feedback = data.get('feedback')

#             # ✅ 필수값 누락 방어
#             if not all([user_id, turn_raw, feedback]):
#                 print('[🚫 필수값 누락]')
#                 return JsonResponse({'error': 'Invalid data'}, status=400)

#             turn = int(turn_raw)

#             # ✅ 로그 출력
#             print(f"[📨 피드백 요청] user_id={user_id}, turn={turn}, feedback={feedback}")

#             # ✅ ChatLog 조회
#             chat = ChatLog.objects.filter(user_id=user_id, turn=turn).first()

#             if not chat:
#                 print("[🚫 ChatLog 없음 → 404 반환]")
#                 return JsonResponse({'error': 'Chat record not found'}, status=404)

#             # ✅ 피드백 저장
#             chat.feedback = feedback
#             chat.save()
#             print("[✅ 피드백 저장 완료]")
#             return JsonResponse({'status': 'ok'})

#         except Exception as e:
#             print("[❌ 예외 발생]", str(e))
#             return JsonResponse({'error': str(e)}, status=500)

#     print("[🚫 잘못된 요청 방식]")
#     return JsonResponse({'error': 'Invalid request method'}, status=405)
@csrf_exempt
def save_feedback_view(request):
    print(f"[💬 피드백 요청 수신] URL: {request.path} | Method: {request.method}")

    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            user_id = data.get('user_id')
            turn_raw = data.get('turn')
            feedback = data.get('feedback')

            print(f"[🕐 피드백 요청 시각] {datetime.now()}")
            print(f"[📨 요청 값] user_id={user_id}, turn={turn_raw}, feedback={feedback}")
            print("[📦 요청 본문]", json.dumps(data, indent=2))

            if not all([user_id, turn_raw, feedback]):
                print('[🚫 필수값 누락]')
                return JsonResponse({'error': 'Invalid data'}, status=400)

            turn = int(turn_raw)

            chat = ChatLog.objects.filter(user_id=user_id, turn=turn).first()

            if not chat:
                print("[🚫 ChatLog 없음]")
                return JsonResponse({'error': 'Chat record not found'}, status=404)

            chat.feedback = feedback
            chat.save()
            chat.refresh_from_db()
            print(f"[💾 저장 완료] feedback = {chat.feedback}")

            return JsonResponse({'status': 'ok'})

        except Exception as e:
            print("[❌ 예외 발생]", str(e))
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Invalid request method'}, status=405)
