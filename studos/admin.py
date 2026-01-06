from django.contrib import admin
from .models import AssistanceRequest

@admin.register(AssistanceRequest)
class AssistanceRequestAdmin(admin.ModelAdmin):
    # This controls the columns you see in the list
    list_display = ('name', 'email', 'phone', 'service', 'submitted_at')
    
    # This allows you to click on the name to open the full message
    list_display_links = ('name', 'email')
    
    # Add filters for easier sorting
    list_filter = ('service', 'submitted_at')
    
    # Enable search
    search_fields = ('name', 'email', 'phone', 'message')