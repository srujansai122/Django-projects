from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils import timezone
from .managers import ItemManager
# Create your models here.
class Item(models.Model):
    
    # def get_absolute_url(self):
    #     return reverse("food:index")
    
    class Meta:
        indexes=[
            models.Index(fields=['user_name','item_price'])
        ]
    
    def __str__(self):
        return self.item_name
    
    def delete(self,using=None,keep_parents=False):
        self.is_deleted=True
        self.deleted_at=timezone.now()
        self.save()
    
    user_name= models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    item_image=models.URLField(max_length=500,default="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRLi8423a2GdO2yi0Ig5N2iRQ8gkCd-F4KTFQ&s")
    item_name= models.CharField(max_length=100,db_index=True)
    item_desc=models.CharField()
    item_price=models.DecimalField(max_digits=6,decimal_places=2,db_index=True)
    is_available=models.BooleanField(default=True)
    created_at=models.DateTimeField(auto_now=True)
    is_deleted=models.BooleanField(default=False)
    deleted_at=models.DateTimeField(null=True,blank=True)
    
    objects=ItemManager()
    all_objects=models.Manager()
    