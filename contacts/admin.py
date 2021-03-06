from django.contrib import admin
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'mobile', 'timing')
    list_display_links = ('name', 'mobile')
    list_per_page = 25
    search_fields = ('name', 'mobile', 'email', 'timing')

admin.site.register(Contact, ContactAdmin)
