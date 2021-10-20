from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.hashers import make_password

class UserManager(BaseUserManager):
   
    def create_user(self, email, user_name, first_name, password, **other_fields):

        if not email:
            raise ValueError('El usuario debe tener un Email')

        email = self.normalize_email(email) 
        user = self.model(email=email, user_name = user_name, first_name=first_name, **other_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, user_name, first_name, password, **other_fields):
        user = self.create_user(email, user_name, first_name, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user        

class NewUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(primary_key=True,unique=True)
    user_name = models.CharField(max_length=200,unique=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    is_staff = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name', 'first_name']
    objects = UserManager()

    def __str__(self):
        return self.user_name


