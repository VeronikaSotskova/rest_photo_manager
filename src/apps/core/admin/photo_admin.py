from django.contrib import admin

from src.apps.core.models import Photo


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'file', 'date_created')
    list_filter = ('user', 'date_created')
