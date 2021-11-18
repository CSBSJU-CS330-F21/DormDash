from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
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




class Customer(models.Model):
    email = models.CharField(max_length=200, null=True)  
    #username = models.CharField(max_length=200, null=True)  
    password = models.IntegerField()
    phone_number = models.CharField(max_length=15)
    address = models.TextField()

    #def get_username(self):
        #return NullBooleanField

    def get_email(self):
        return NullBooleanField
    
    def get_phoneNumber(self):
        return NullBooleanField

    def get_is_login(self):
        return self.is_login

class Driver(models.Model):
    email = models.CharField(max_length=200, null=True)
    password = models.IntegerField()
    phone_number = models.CharField(max_length=15)
    delivery_address = models.TextField()

    def get_email(self):
        return NullBooleanField
    
    def get_phoneNumber(self):
        return NullBooleanField

    def get_is_login(self):
        return self.is_login


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    phone_number = models.CharField(max_length=15)
    address = models.TextField()

    def __str__(self):
        return self.user.username

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


'''
# Create your models here.
USER_TYPE = (
    (1, 'customer'),
    (2, 'driver'),
)

class User(AbstractBaseUser, PermissionsMixin):
    username = None
    email = models.EmailField(('email address'), unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    #email = models.EmailField(max_length=255)
    #email_verified = models.BooleanField(default=False)
    #activation_code = models.CharField(max_length=100, null=True, blank=True)
    #is_active = models.BooleanField(default=False)
    password = models.IntegerField()
    phone_number = models.CharField(max_length=15)
    #user_type = models.CharField(choices=USER_TYPE, max_length=10)
    #is_admin = models.BooleanField(default=False)
    is_driver = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)
    is_login = models.BooleanField(default=False)

    objects = UserManager

    def get_email(self):
        return NullBooleanField
    
    def get_phoneNumber(self):
        return NullBooleanField

    def get_is_login(self):
        return self.is_login

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    address = models.TextField()

    def get_deliveryAddress(self):
        return NullBooleanField

class Driver(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    delivery_address = models.TextField()
'''