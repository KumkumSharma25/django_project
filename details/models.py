from django.db import models

# Create your models here.
class Dynamic(models.Model):
    dynamic_title=models.CharField(max_length=150)
    dynamic_desc=models.TextField()
    dynamic_img_link=models.CharField(max_length=150)
    dynamic_read_link=models.CharField(max_length=150)
    dynamic_imgg = models.FileField(upload_to="media",max_length=250,null=True,default=None)