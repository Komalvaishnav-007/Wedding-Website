from django.contrib import admin

# Register your models here.
from ourguardsnew.models import Ourguards
class OurguardsAdmin(admin.ModelAdmin):
    list_display=('Ourguards_placename','Ourguards_post','Ourguards_img')
admin.site.register(Ourguards,OurguardsAdmin)
