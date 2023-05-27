from django.contrib import admin
from .models import Type, Status, Issue
# Register your models here.
admin.site.register(Type)
admin.site.register(Status)
admin.site.register(Issue)