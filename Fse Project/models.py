from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# Create your models here.
class contact(models.Model):
    sno = models.AutoField(primary_key=True)
    fullname = models.CharField(max_length=255)
    email = models.CharField(max_length=100)
    content=models.TextField()
    timestamp=models.DateTimeField(auto_now_add=True,blank=True)
    
    def __str__(self):
        return 'Message from' + self.fullname
    
class uploadcode(models.Model):
        file = models.FileField(upload_to='uploads/')
        uploaded_at = models.DateTimeField(auto_now_add=True)
        
 
        


class UserManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    email = models.EmailField(verbose_name='email address', max_length=255, unique=True)
    username = models.CharField(max_length=30, unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_superuser(self):
        return self.is_admin
        