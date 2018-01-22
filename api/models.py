# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

class Prognose(models.Model):

    sector = models.CharField(max_length=1023, blank=True, null=True)
    branche = models.CharField(max_length=1023, blank=True, null=True)
    head = models.CharField(max_length=1023, blank=True, null=True)
    body = models.CharField(max_length=1023, blank=True, null=True)
    prog_id = models.IntegerField(primary_key=True)     

    class Meta:
        managed = False
        db_table = 'prog_table'

class Trend(models.Model):
    sector = models.CharField(max_length=1023, blank=True, null=True)
    branche = models.CharField(max_length=1023, blank=True, null=True)
    head = models.CharField(max_length=1023, blank=True, null=True)
    body = models.CharField(max_length=1023, blank=True, null=True)
    trend_id = models.IntegerField(primary_key=True)     

    class Meta:
        managed = False
        db_table = 'trend_table'

class Info(models.Model):
    sector = models.CharField(max_length=1023, blank=True, null=True)
    branche = models.CharField(max_length=1023, blank=True, null=True)    
    body = models.CharField(max_length=1023, blank=True, null=True)
    info_id = models.IntegerField(primary_key=True)     

    class Meta:
        managed = False
        db_table = 'info_table'

class PrognoseEffect(models.Model):    
    body = models.CharField(max_length=1023, blank=True, null=True)
    prog_id = models.IntegerField(primary_key=True)     

    class Meta:
        managed = False
        db_table = 'prog_eff_table'

class TrendEffect(models.Model):    
    body = models.CharField(max_length=1023, blank=True, null=True)
    trend_id = models.IntegerField(primary_key=True)     

    class Meta:
        managed = False
        db_table = 'trend_eff_table'

class Devel_for_branche(models.Model):    
    branche = models.CharField(max_length=1023, blank=True, null=True)
    devel_id = models.IntegerField()
    rowid = models.IntegerField(primary_key=True)     

    class Meta:
        managed = False
        db_table = 'devel_for_branche'

class Development(models.Model):    
    development = models.CharField(max_length=1023, blank=True, null=True)
    rowid = models.IntegerField(primary_key=True)     

    class Meta:
        managed = False
        db_table = 'development_table'

class DevEffect(models.Model):    
    body = models.CharField(max_length=1023, blank=True, null=True)
    dev_id = models.IntegerField(primary_key=True)     

    class Meta:
        managed = False
        db_table = 'dev_eff_table'

class Requested_Dev(models.Model):
    development = models.CharField(max_length=1023, blank=True, null=True)
    user = models.CharField(max_length=1023, blank=True, null=True)
    date = models.CharField(max_length=1023, blank=True, null=True)
    rowid = models.IntegerField(primary_key=True)     

    class Meta:
        managed = False
        db_table = 'requested_developments'

class Scenario(models.Model):
    developments = models.CharField(max_length=1023, blank=True, null=True)
    user = models.CharField(max_length=1023, blank=True, null=True)
    date_created = models.CharField(max_length=1023, blank=True, null=True)
    date_estimated = models.CharField(max_length=1023, blank=True, null=True)
    turn_over = models.IntegerField()
    ebitda = models.IntegerField()
    bruto_margin = models.IntegerField() 
    liquidity = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'scenario_table'