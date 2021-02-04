from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin


class UserManager(BaseUserManager):
    def create_user(self,email,password=None, **extra_fields):
        """Create and Save a new User"""
        user = self.model(email= self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user
    def create_superuser(self,email,password=None, **extra_fields):
        """Create and Save a new User"""
        user = self.model(email= self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.is_superuser = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser,PermissionsMixin):
    """Custom user model """
    email = models.EmailField(max_length=255,unique=True)
    name = models.CharField(max_length=255)
    gender = models.BooleanField(default=True) #True : male, False: Female
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'