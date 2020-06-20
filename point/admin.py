from django.contrib import admin

# Register your models here.
from .models import score,record

admin.site.register(score)
admin.site.register(record)