from django.contrib import admin
from .models import Project


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'date')
    list_display_links = ('title',)
    search_fields = ('title', 'description')
    list_per_page = 10


admin.site.register(Project, ProjectAdmin)
