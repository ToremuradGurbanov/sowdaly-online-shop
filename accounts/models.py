from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db.models.fields.related import RECURSIVE_RELATIONSHIP_CONSTANT


class MyAccountManager(BaseUserManager):
    
    def create_user(self,username, first_name, last_name, email, password=None):
        if not email:
            raise ValueError('User should have an email address')
    
        user = self.model(
            email = self.normalize_email(email),
            first_name = first_name,
            last_name = last_name,
            username = username,
        )       
        user.set_password(password)
        user.save(using=self._db)
        
        return user
        
    def create_superuser(self,first_name , last_name , username, email, password):

        user = self.create_user(
            email = self.normalize_email(email),
            password = password,
            username = username,
            first_name= first_name,
            last_name = last_name,
            
        )
        user.is_admin = True
        user.is_staff = True
        user.is_active = True
        user.is_superadmin= True

        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    username = models.CharField(max_length=40, unique=True)
    email = models.EmailField(max_length=70, unique=True)
    phone_number = models.CharField(max_length=40)


    ## required 
    date_join = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)
    
    objects = MyAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    

    def __str__(self):
        return self.email


    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, add_label):
        return True
