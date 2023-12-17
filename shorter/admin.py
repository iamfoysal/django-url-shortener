from django.contrib import admin
from .models import Url

class UrlAdmin(admin.ModelAdmin):
    list_display = ('original_url', 'short_code', 'clicks','last_click')
    ordering = ('-clicks',)



admin.site.register(Url, UrlAdmin)