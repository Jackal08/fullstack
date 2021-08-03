from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("Hello, world. 37fa3f03 You're at the polls index.")
