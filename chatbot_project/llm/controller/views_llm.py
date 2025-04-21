from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from llm.service.llm_service import LLMService

@csrf_exempt
def ask_llm(request):
    if request.method == 'POST':
        companies = request.POST.getlist('companies')         # ["AXA", "KB"]
        categories = request.POST.getlist('categories')       # ["암보험"]
        question = request.POST.get('query')                  # "암 진단시 얼마를 받나요?"

        llm_service = LLMService()
        answer = llm_service.generate_answer_with_filtering(question, companies, categories)

        return JsonResponse({'answer': answer})
