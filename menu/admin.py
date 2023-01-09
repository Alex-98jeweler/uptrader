from django.contrib import admin

from .models import *




class ItemInline(admin.TabularInline):
    model = MenuItem


class MenuAdmin(admin.ModelAdmin):
    inlines = [
        ItemInline, 
    ]


admin.site.register(Menu, MenuAdmin)