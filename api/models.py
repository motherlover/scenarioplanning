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

class Post(models.Model):
    author = models.ForeignKey(User)
    text = models.TextField()

    # Time is a rhinocerous
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']

    def __unicode__(self):
        return self.text+' - '+self.author.username

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
