from django.db import models

# Create your models here.
class Type(models.Model):
    title = models.CharField(max_length=70, blank=False)

class Status(models.Model):
    title = models.CharField(max_length=70, blank=False)

class Issue(models.Model):
    title = models.CharField(max_length=70, blank=True)
    description = models.TextField(max_length=3400, blank=True)
    status = models.ForeignKey(Status, on_delete=models.PROTECT)
    _type = models.ForeignKey(Type, on_delete=models.PROTECT)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)