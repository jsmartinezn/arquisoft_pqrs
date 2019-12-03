from django.core.cache import cache
from django.http import HttpResponse
from .models import contenido
from datetime import datetime
def registrar(request,tipo,idU,contenid):
    a = cache.get(0)
    b = contenido(idP=str(a),mensaje=contenid,idUsuario=idU,tipo=tipo,fecha=str(datetime.now()),estado="recibida",respuesta="")
    cache.set(a, b)
    a = a+1
    cache.set(0,a)
    return HttpResponse('funciono')

def darSolicitud(request,id):
    print(cache.get(id))
    return HttpResponse('el contenido de la '+cache.get(id).tipo+" presentada por el usuario con id "+ str(cache.get(id).idUsuario)+" es: " + cache.get(id).mensaje)

def cambiarEstado(request,id):
    a=cache.get(id)
    b=contenido(idP=a.idP,mensaje=a.mensaje,idUsuario=a.idUsuario,tipo=a.tipo,fecha=a.fecha,estado="solucionada",respuesta=a.respuesta)
    cache.set(id,b)
    return HttpResponse('se actualizo el estado a:'+ cache.get(id).estado)

def responder(request,id,respuesta):
    a=cache.get(id)
    b=contenido(idP=a.idP,mensaje=a.mensaje,idUsuario=a.idUsuario,tipo=a.tipo,fecha=a.fecha,estado=a.estado,respuesta=respuesta)
    cache.set(id, b)
    return HttpResponse('se actualizo la respuesta a:'+ cache.get(id).respuesta)