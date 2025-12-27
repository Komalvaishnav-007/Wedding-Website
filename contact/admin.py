from django.contrib import admin
from contact.models import Contact
# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'email', 'phone', 'message','no_of_guests')
admin.site.register(Contact, ContactAdmin)
