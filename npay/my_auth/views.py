from django.http import HttpResponse


def home(request):
    return HttpResponse("Hello, welcome to my Django Dennis app!")


def register(request):
    return HttpResponse("Hello, register to nullchemy pay")
