from django.db import models

class DualDeskRequest(models.Model):
    user = models.CharField(max_length=255)
    unit = models.IntegerField()


class Cliente(models.Model):
    id = models.BigIntegerField(primary_key=True)
    nombre = models.CharField(max_length=50, blank=True, null=True)
    nombredb = models.CharField(max_length=50, blank=True, null=True)
    fechacreacion = models.DateTimeField(blank=True, null=True)
    schema_name = models.CharField(max_length=250, blank=True, null=True)
    logo = models.CharField(max_length=250, blank=True, null=True)
    user_group = models.CharField(max_length=250, blank=True, null=True)
    pagos = models.CharField(max_length=250, blank=True, null=True)
    mascara = models.BooleanField(blank=True, null=True)
    mascara_tipo = models.CharField(max_length=250, blank=True, null=True)
    no_contact = models.BooleanField(blank=True, null=True)
    wolkvox = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cliente'


class Unidad(models.Model):
    id = models.BigIntegerField(primary_key=True)
    idcliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='idcliente', blank=True, null=True)
    nombre = models.CharField(max_length=150, blank=True, null=True)
    fechacreacion = models.DateTimeField(blank=True, null=True)
    vicidial = models.CharField(max_length=120, blank=True, null=True)
    prefijo = models.IntegerField(blank=True, null=True)
    call_return = models.CharField(max_length=250, blank=True, null=True)
    in_charge = models.BigIntegerField(blank=True, null=True)
    surveys = models.CharField(max_length=250, blank=True, null=True)
    virtual_agent = models.BooleanField(blank=True, null=True)
    inbound_number = models.BooleanField(blank=True, null=True)
    dual = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'unidad'
