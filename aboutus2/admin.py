from django.contrib import admin

# Register your models here.
from aboutus2.models import Aboutus2
class Aboutus2Admin(admin.ModelAdmin):
 list_display=('Aboutus2_title','Aboutus2_desc','Aboutus2_read_link','Aboutus2_img')
admin.site.register(Aboutus2,Aboutus2Admin)