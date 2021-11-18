from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.fields import NullBooleanField
from django.db import models
from django.contrib.auth.models import User

'''
class menuItem(models.Model):
    name = models.TextField()
    foodPic = models.ImageField(upload_to='images/')

    def get_name(self):
        return self.name

    def get_fields(self):
        return [(field.name, getattr(self,field.name)) for field in menuItem._meta.fields]

    def upload_image(self, filename):
        return 'menuItem/{}/{}'.format(self.title, filename)

class OrderDetails(models.Model):
    name = models.TextField()
    menuItem = models.ForeignKey('menutItem', related_name='menuItem')
    quantity = models.PositiveIntegerField()
    price = models.FloatField()
    def get_name(self):
        return self.name

    def get_fields(self):
        return [(field.name, getattr(self,field.name)) for field in OrderDetails._meta.fields]
'''

class Order(models.Model):
    name = models.TextField()
    addressStore = models.TextField()
    campus = models.TextField()
    address = models.TextField()
    def get_name(self):
        return self.name
    def get_fields(self):
        return [(field.name, getattr(self,field.name)) for field in Order._meta.fields]



class Restaurant(models.Model):
    name = models.TextField()
    address = models.TextField()
    restaurant_pic = models.ImageField(upload_to='images/')

    def get_name(self):
        return self.name

    def get_fields(self):
        return [(field.name, getattr(self,field.name)) for field in Restaurant._meta.fields]

    def upload_image(self, filename):
        return 'restaurant/{}/{}'.format(self.title, filename)



class User(AbstractUser):
    is_customer = models.BooleanField(default=False)
    is_driver = models.BooleanField(default=False)

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField

    def __str__(self):
        return self.user.username

class Driver(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    def __str__(self):
        return self.user.username

