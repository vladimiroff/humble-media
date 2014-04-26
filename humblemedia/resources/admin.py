from django.contrib import admin

# Register your models here.
from . import models


class AttachmentAdmin(admin.ModelAdmin):
    list_display = ('document_', )


admin.site.register(models.Attachment, AttachmentAdmin)
admin.site.register(models.Resource, admin.ModelAdmin)
