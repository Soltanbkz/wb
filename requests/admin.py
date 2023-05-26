from django.contrib import admin

from requests.models import Contact


# Register your models here.
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'email', 'phone_number', 'message', 'date_created')
    list_filter = ('id','date_created', 'name', 'email')
    search_fields = ('id','date_created', 'name', 'email')
