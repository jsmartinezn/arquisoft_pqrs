from django.core.cache import cache
from django.http import HttpResponse
from django.db import models

def inicio(request):
    cache.set(0,1)
    return HttpResponse('se inicializo')

