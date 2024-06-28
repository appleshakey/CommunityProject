from django.db import models
from django.contrib.auth.models import UserManager, AbstractBaseUser, PermissionsMixin
from django.conf import settings
from django.utils import timezone
import uuid

class CustomUserManager(UserManager):
    def _create_user(self, email, password, **kwargs):
        email = self.normalize_email(email)
        user = self.model(email = email, **kwargs)
        user.set_password(password)
        user.save()
        return user
    
    def create_user(self, email = None, password = None, **kwargs):
        kwargs.setdefault('is_staff', False)
        kwargs.setdefault('is_superuser', False)
        return self._create_user(email, password, **kwargs)
    
    def create_superuser(self, email = None, password = None, **kwargs):
        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_superuser', True)
        return self._create_user(email, password, **kwargs)
    
class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key = True, editable = False, default = uuid.uuid4)
    email = models.EmailField(blank = True, default = '', unique = True)
    name = models.CharField(max_length = 255, blank = True, default = '')
    contact = models.PositiveBigIntegerField(blank = True, null = True)
    is_active = models.BooleanField(default = True)
    is_superuser = models.BooleanField(default = False)
    is_staff = models.BooleanField(default = False)

    date_joined = models.DateTimeField(default = timezone.now)
    last_login = models.DateTimeField(blank = True, null = True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'User'
        verbose_name = 'Users'

    def get_full_name(self):
        return self.name
