from django.http import HttpResponse

def index(request):
    return HttpResponse("시 하이")