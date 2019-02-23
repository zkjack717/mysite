from django.contrib import admin
from .models import LikeRecord, LikeCount

# Register your models here.


@admin.register(LikeRecord)
class LikeCountAdmin(admin.ModelAdmin):
    list_display = ('content_type', 'object_id', 'content_object')


@admin.register(LikeCount)
class LikeRecord(admin.ModelAdmin):
    list_display = ('content_type', 'object_id', 'content_object')
