from django.contrib import admin
from .models import *
class DotaAdmin(admin.ModelAdmin):
    list_display = ('id', 'title','photo')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
admin.site.register(Dota, DotaAdmin)



