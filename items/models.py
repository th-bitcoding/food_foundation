from django.db import models
from base.models import MyModel
from customeuser.models import CustomeUser
# Create your models here.
class Category(MyModel):
    category_name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Items(MyModel):
    username = models.ForeignKey(CustomeUser,on_delete=models.CASCADE)
    item_name = models.ForeignKey(Category,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='item/')
    quantity = models.IntegerField()

    def __str__(self):
        return self.username.username
