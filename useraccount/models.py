from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager
from django.core.validators import MinLengthValidator, MaxLengthValidator, RegexValidator

# Create your models here.


class UserManager(BaseUserManager):
    def create_user(self, email, username=None, password=None,  *args, **kwargs):
        if not email:
            raise ValueError("Users must have an email address")
        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user
        

    def create_superuser(self, email, password, username=None, *args, **kwargs):
        user = self.create_user(email=email,password=password)
        user.set_password(password)
        user.is_staff = True
        user.is_active = True
        user.save(using=self._db)
        return user
    



class User(AbstractBaseUser):
    email = models.EmailField(unique=True, validators=[MaxLengthValidator(254)])
    password = models.CharField(max_length=128, validators=[MinLengthValidator(8)])
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone = models.CharField(max_length=10, validators=[RegexValidator(r'^\d{10}$', message='Phone number must be 10 digits.')])
    address = models.CharField(max_length=100, blank=True,null=True)
    city = models.CharField(max_length=50, blank=True,null=True)
    state = models.CharField(max_length=50, blank=True,null=True)
    country = models.CharField(max_length=50, blank=True,null=True)
    pincode = models.CharField(max_length=6, validators=[RegexValidator(r'^\d{6}$', message='Pincode must be 6 digits.')])
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False,blank=True)
    is_blocked = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    date_joined = models.DateField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = "email"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = []

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        return True



class Content(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='contents',null=True)
    title = models.CharField(max_length=30, validators=[MaxLengthValidator(30)])
    body = models.TextField(max_length=300)
    summary = models.CharField(max_length=60, validators=[MaxLengthValidator(60)])
    document = models.FileField(upload_to='userfiles/documents/', null=True, blank=True)
    categories = models.ManyToManyField('Category')
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name