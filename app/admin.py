from django.contrib import admin
from .models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display  = ('title', 'subtitle', 'is_wide', 'is_active', 'order')
    list_editable = ('is_wide', 'is_active', 'order')
    search_fields = ('title', 'subtitle')
    list_filter   = ('is_active', 'is_wide')
    fields        = ('title', 'subtitle', 'video_file', 'video_url', 'is_wide', 'is_active', 'order')
