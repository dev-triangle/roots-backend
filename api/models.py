from distutils.command.upload import upload
from email.policy import default
from django.db import models
from django.contrib.auth.models import (AbstractBaseUser,BaseUserManager,PermissionsMixin)
# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self,username,email,password=None):
        if username is None:
            raise TypeError("Users should have a username")

        if email is None:
            raise TypeError("Users should have a email")

        user=self.model(username=username,email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,username,email,password=None):
        if password is None:
            raise TypeError("Password should not be none")
        
        user=self.create_user(username,email,password)
        user.is_superuser=True
        user.is_staff=True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser,PermissionsMixin):
    username=models.CharField(max_length=255,unique=True,db_index=True)
    email=models.EmailField(max_length=255,unique=True,db_index=True)
    is_verified=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['username']

    objects=UserManager()
    def __str__(self):
        return self.username

    def tokens(self):
        return ''

class Trending(models.Model):
    place_name=models.CharField(max_length=100)
    place_image=models.ImageField(upload_to='trending_images')
    place_location=models.CharField(max_length=100)
    trending_item=models.CharField(max_length=100)

    def __str__(self):
        return self.place_name

class Place(models.Model):
    place_name=models.CharField(max_length=100)
    place_image=models.ImageField(upload_to='place_images')
    place_description=models.TextField(max_length=1000)

    def __str__(self):
        return self.place_name

class Activities(models.Model):
    activity_name=models.CharField(max_length=100)
    activity_image=models.ImageField(upload_to='activity_images')
    place_foreign=models.ForeignKey(Place,on_delete=models.CASCADE)
    activity_description=models.TextField(max_length=1000)

    def __str__(self):
        return(self.activity_name)

class Festival(models.Model):
    festival_name=models.CharField(max_length=100)
    festival_desc=models.TextField(max_length=300)
    place_foreign=models.ForeignKey(Place,on_delete=models.CASCADE)
    festival_image=models.ImageField(upload_to='festival_image',blank=True,null=True)

    def __str__(self):
        return(self.festival_name)
    
class Item(models.Model):
    item_name=models.CharField(max_length=100)
    place_foreign=models.ForeignKey(Place,on_delete=models.CASCADE)
    item_desc=models.TextField(max_length=300)
    item_image=models.ImageField(upload_to='item_image',blank=True,null=True)

    def __str__(self):
        return(self.item_name)
    
class Guide(models.Model):
    guide_name=models.CharField(max_length=100)
    guide_image=models.ImageField(upload_to='guide_images',blank=True,null=True)
    place_foreign=models.ForeignKey(Place,on_delete=models.CASCADE)
    guide_description=models.TextField(max_length=200)

    def __str__(self):
        return(self.guide_name)

class Purchase(models.Model):
    item_foreign_key=models.ForeignKey(Item,on_delete=models.CASCADE)
    user_foreign=models.ForeignKey(User,on_delete=models.CASCADE)
    date_of_purchase=models.DateField()

    def __str__(self):
        return(self.item_foreign_key)
    
class Attraction(models.Model):
    place_foreign=models.ForeignKey(Place,on_delete=models.CASCADE)
    name=models.CharField(max_length=20)
    image=models.ImageField(upload_to='attractions_images',blank=True,null=True)
    desc=models.TextField(max_length=500)
    contact_number=models.CharField(max_length=100)

    def __str__(self):
        return (self.name)
