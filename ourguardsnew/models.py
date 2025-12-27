from django.db import models

# Create your models here.
class Ourguards(models.Model):
  Ourguards_placename=models.CharField( max_length=250)
  Ourguards_post=models.CharField( max_length=250)
  Ourguards_img=models.FileField(upload_to="ourguards", max_length=250, null=True,default=None )