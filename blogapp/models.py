from django.db import models

# Create your models here.

class Articles(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=250)
    description = models.TextField()
    image = models.ImageField(upload_to='articleimage')
    slug = models.SlugField(max_length=500)
    author = models.CharField(max_length=100)
    
    def __str__(self):
        return self.title
