from django.contrib import admin
from part.models import Part


class PartAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "status", "auto", "last_time")


admin.site.register(Part, PartAdmin)
