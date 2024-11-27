from django.db import models

class Tym(models.Model):
    nazev = models.CharField(max_length=255)
    vyhry = models.IntegerField(default=0)
    prohry = models.IntegerField(default=0)
    remizy = models.IntegerField(default=0)

class Hrac(models.Model):
    jmeno = models.CharField(max_length=255)
    prijmeni = models.CharField(max_length=255)
    tym = models.ForeignKey(Tym, on_delete=models.CASCADE)
    goly = models.IntegerField(default=0)
    asistence = models.IntegerField(default=0)

class Zapas(models.Model):
    tym_a = models.ForeignKey(Tym, related_name='zapasy_tym_a', on_delete=models.CASCADE)
    tym_b = models.ForeignKey(Tym, related_name='zapasy_tym_b', on_delete=models.CASCADE)
    datum = models.DateField()
    goly_tym_a = models.IntegerField(default=0)
    goly_tym_b = models.IntegerField(default=0)

class StatistikyZapasu(models.Model):
    zapas = models.ForeignKey(Zapas, on_delete=models.CASCADE)
    hrac = models.ForeignKey(Hrac, on_delete=models.CASCADE)
    goly = models.IntegerField(default=0)
    asistence = models.IntegerField(default=0)
    zlte_karty = models.IntegerField(default=0)
    cervene_karty = models.IntegerField(default=0)
