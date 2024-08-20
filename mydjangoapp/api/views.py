from django.http import JsonResponse

def api_home(request):
    return JsonResponse({"message": "Welcome to the API!"})

def api_data(request):
    data = {
        "name": "John Doe",
        "age": 30,
        "location": "Boston"
    }
    return JsonResponse(data)
