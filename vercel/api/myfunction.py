from django.http import JsonResponse

def my_function(request):
    # 处理动态请求的代码
    return JsonResponse({'message': 'Hello from Djangi serverless function!'})