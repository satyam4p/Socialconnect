from django.contrib import admin
from . import models
# Register your models here.

class groupmememberInline(admin.TabularInline):
    model=models.groupmember

admin.site.register(models.group)
