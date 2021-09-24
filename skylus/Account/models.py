from django.contrib.auth.hashers import make_password
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.mail import send_mail
from django.db.models.fields import EmailField
from django.utils import timezone
from django.apps import apps
# Create your models here.


class CustomUserManager(BaseUserManager):
    use_in_migrations = True
    def _create_user(self, username,domain_name,password, email,**extra_fields):
        if not username:
            raise ValueError('The Given username must be set')
        email = self.normalize_email(email)
        GlobalUserModel = apps.get_model(self.model._meta.app_label, self.model._meta.object_name)
        username = GlobalUserModel.normalize_username(username)
        user = self.model(username=username, domain_name=domain_name,email=email,**extra_fields)
        user.password = make_password(password)
        user.save(using=self.db)
        return user

    def create_user(self, username, domain_name=None,email = None, password=None,**extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, domain_name, email, password,**extra_fields)

    def create_superuser(self,username, domain_name=None, email= None,password=None,**extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=true')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Super User must have is_superuser=true')
        # user = self.model(username=username, domain_name=domain_name)
        # user.password = make_password(password)
        # user.save(using=self.db)
        # return user
        return self._create_user(username, domain_name, email, password,**extra_fields)
        


class SkylusUser(AbstractBaseUser):
    username = models.CharField(max_length=150,unique=True,error_messages={
            'unique':("A user with that username already exists."),
        },)
    domain_name = models.CharField(max_length=100)
    email = models.EmailField()
    is_staff = models.BooleanField(('staff status'),default=False,help_text=('Designates whether the user can log into this admin site.'),)
    is_active = models.BooleanField(('active'),default=True,help_text=(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    date_joined = models.DateTimeField(('date joined'), default=timezone.now)

    objects = CustomUserManager()
    EMAIL_FIELD='email'

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['domain_name',]

    # class Meta:
    #     verbose_name =('user')
    #     verbose_name_plural =('users')
    #     abstract = True

    # def clean(self):
    #     super().clean()
    #     self.email = self.__class__.objects.normalize_email(self.email)

    # def get_full_name(self):
    #     """
    #     Return the first_name plus the last_name, with a space in between.
    #     """
    #     full_name = '%s %s' % (self.first_name, self.last_name)
    #     return full_name.strip()

    # def get_short_name(self):
    #     """Return the short name for the user."""
    #     return self.first_name

    # def email_user(self, subject, message, from_email=None, **kwargs):
    #     """Send an email to this user."""
    #     send_mail(subject, message, from_email, [self.email], **kwargs)

