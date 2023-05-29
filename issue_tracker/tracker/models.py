from django.db import models

# Create your models here.
class Type(models.Model):
    type = models.CharField(max_length=70, blank=False)

    def __str__(self):
        return self.type

class Status(models.Model):
    status = models.CharField(max_length=70, blank=False)

    def __str__(self):
        return self.status

class Issue(models.Model):
    title = models.CharField(max_length=70, blank=True)
    description = models.TextField(max_length=3400, blank=True)
    status = models.ForeignKey(Status, on_delete=models.PROTECT)
    type = models.ForeignKey(Type, on_delete=models.PROTECT)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    is_closed = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def delete(self):
        self.is_closed = True
        self.save()