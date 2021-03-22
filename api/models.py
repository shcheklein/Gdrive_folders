from django.db import models
from solo.models import SingletonModel


class Test(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)


class Config(SingletonModel):

    folder_informe_id = models.CharField(max_length=256, blank=True, verbose_name="ID carpeta Informes")
    folder_relevamiento_id = models.CharField(max_length=256, blank=True, verbose_name="ID carpeta relevamientos")
    sheet_id = models.CharField(max_length=256, blank=True, verbose_name="ID planilla gestion")
    remito_col = models.CharField(max_length=256, blank=True, verbose_name="Numero de columna remito")
    informe_col = models.CharField(max_length=256, blank=True, verbose_name="Numero de columna informe")
    relevamientos_col = models.CharField(max_length=256, blank=True, verbose_name="Numero de columna relevamientos")


class Cliente(models.Model):

    nombre = models.CharField(max_length=300)
    correo1 = models.EmailField(blank=True, null=True)
    correo2 = models.EmailField(blank=True, null=True)
    correo3 = models.EmailField(blank=True, null=True)
    correo4 = models.EmailField(blank=True, null=True)
    correo5 = models.EmailField(blank=True, null=True)
    correo6 = models.EmailField(blank=True, null=True)
    id_cliente = models.CharField(max_length=50, unique=True, primary_key=True)


class Tarea (models.Model):
    remito = models.CharField(max_length=100, unique=True, primary_key=True)
    id_cliente = models.CharField(max_length=100)
    tipo_estudio = models.CharField(max_length=100)
    timestamp = models.DateTimeField(null=True, blank=True)
    is_send = models.BooleanField(default=False)
    aprobado2 = models.CharField(max_length=300)





