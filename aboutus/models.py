from django.db import models

# Create your models here.
class Aboutus (models.Model):
 Aboutus_title=models.CharField( max_length=150)
 Aboutus_desc=models.TextField()
 Aboutus_read_link=models.CharField( max_length=150)
 Aboutus_img=models.FileField(upload_to="aboutus", max_length=250, null=True,default=None )