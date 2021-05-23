from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _
from .managers import UserManager


def user_directory_path(instance, filename):
    # file will be uploaded to media/users/avatars/user_<email>/<filename>
    return 'users/avatars/{0}/{1}'.format(instance.email, filename)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    name = models.CharField(_('name'), max_length=30)
    phone = models.CharField(_('phone'), max_length=20)
    address = models.CharField(_('address'), max_length=50)
    is_active = models.BooleanField(_('is active'), default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(_('is super'), default=False)
    last_login = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(_('date created'), auto_now_add=True)
    updated_at = models.DateTimeField(_('date updated'), auto_now_add=True)
    avatar = models.ImageField(upload_to=user_directory_path, null=True, blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'phone']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
