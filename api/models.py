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
