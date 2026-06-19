from django.db import models
from django.utils.text import slugify
# Create your models here.

class Product(models.Model):
    name=models.CharField(max_length=50)
    price=models.FloatField()
    description=models.TextField()
    image=models.ImageField(upload_to='images/')
    slug=models.SlugField(unique=True,blank=True)
    stock=models.IntegerField()
    active=models.BooleanField(default=True)
    
    def save(self,*args, **kwargs):
        if not self.slug:
            base_slug=slugify(self.name)
            slug=base_slug
            counter=1
            while Product.objects.filter(slug=base_slug).exists():
                slug=f'{base_slug}_{counter}'
                counter+=1
            self.slug=slug
        super().save(*args,**kwargs)