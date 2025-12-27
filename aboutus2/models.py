from django.db import models

# Create your models here.
class Aboutus2 (models.Model):
 Aboutus2_title=models.CharField( max_length=150)
 Aboutus2_desc=models.TextField()
 Aboutus2_read_link=models.CharField( max_length=150)
 Aboutus2_img=models.FileField(upload_to="aboutus2", max_length=250, null=True,default=None )