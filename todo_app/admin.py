from django.contrib import admin
from .models import *


@admin.register(Todo, Pdf)
class DefaultAdmin(admin.ModelAdmin):
    pass
