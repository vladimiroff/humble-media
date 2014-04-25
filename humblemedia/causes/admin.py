from django.contrib import admin

# Register your models here.
from . import models

class CauseAdmin(admin.ModelAdmin):
    list_display = ("title", "creator", "target", "is_verified", "is_published")
    list_editable = ("is_verified", "is_published")

admin.site.register(models.Cause, CauseAdmin)