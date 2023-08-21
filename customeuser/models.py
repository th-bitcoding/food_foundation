from django.db import models
from django.contrib.auth.models import AbstractUser
from base.models import MyModel

# Create your models here.
class CustomeUser(AbstractUser,MyModel):
    type_user_data =(
        (1,'HOD_Admin'),
        (2,'NGO'),
    ) 

    user_type = models.IntegerField(choices=type_user_data,default=1)
    profile_pic=models.ImageField(upload_to='profile')
    address = models.TextField()
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=13)
 
    # specialist = models.ManyToManyField(Disease)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.username