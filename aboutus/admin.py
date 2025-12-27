from django.contrib import admin
# from .models import Aboutus

# Register your models here.
from aboutus.models import Aboutus
class AboutusAdmin(admin.ModelAdmin):
 list_display=('Aboutus_title','Aboutus_desc','Aboutus_read_link','Aboutus_img')
admin.site.register(Aboutus,AboutusAdmin)