from django.contrib import admin
from .models import Package

@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    list_display = ('tracking_id', 'from_location', 'to_location', 'status', 'scheduled_delivery')
    search_fields = ('tracking_id', 'from_location', 'to_location')
