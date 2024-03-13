from django.db import models
import uuid
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, phone, password=None, **extra_fields):
        if not phone:
            raise ValueError('The Phone field must be set')
        user = self.model(phone=phone, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, phone, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        
        return self.create_user(phone, password, **extra_fields)
    
class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField( 
        default=uuid.uuid4, unique=True, editable=False, db_index=True, primary_key=True
    )
    avatar = models.ImageField(upload_to='images/', blank=True)
    job = models.CharField(max_length=50, blank=True)
    bio = models.CharField(max_length=200, blank=True)
    full_name = models.CharField(
        max_length=255, default='', verbose_name="Ism familiya")
    phone = models.CharField(max_length=15, unique=True,
                             verbose_name="Telefon", db_index=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = "phone"

    objects = UserManager()

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
        db_table = "users"
        ordering = ("-is_active",)

    def __str__(self):
        return self.phone
    
class Follow(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="followers", blank=True, null=True)
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name="followings", blank=True, null=True)
    
    
    class Meta:
        unique_together = ('user', 'follower',)

    

