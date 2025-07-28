from django.contrib import admin
from .models import Ticket

# Register your models here.
class TicketAdmin(admin.ModelAdmin):
    list_display = ['website_name', 'title', 'email_address', 'status', 'created_at']
    list_filter = ['status', 'website_name']
    search_fields = ['title', 'description', 'email_address']

admin.site.register(Ticket, TicketAdmin)