from django.db import models

class contenido(models.Model):
    idP = models.CharField(max_length=50)
    mensaje=models.CharField(max_length=100)
    idUsuario=models.CharField(max_length=50)
    tipo=models.CharField(max_length=50)
    fecha=models.CharField(max_length=50)
    estado=models.CharField(max_length=50)
    respuesta=models.CharField(max_length=100)