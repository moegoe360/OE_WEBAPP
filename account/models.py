from django.contrib import auth
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
import uuid
from account.choices import *
from experiment.models import Experiment
from .validator import UnicodeUsernameValidator
from django.utils import timezone
from django.core.exceptions import ValidationError
#from django.forms import extras
#from django.forms.widgets import SelectDateWidget

#from pgcrypto_expressions.fields import *
#from pgcrypto import *

#from fernet_fields import EncryptedTextField

# Create your models here.

class UserManager(BaseUserManager):
    use_in_migrations = True
    
    def _create_user(self, username, email, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        if not username:
            raise ValueError('The given username must be set')
        email = self.normalize_email(email)
        username = self.model.normalize_username(username)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_user(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_participant', True)
        extra_fields.setdefault('is_researcher', False)
        return self._create_user(username, email, password, **extra_fields)
    
    def create_anon_user(self, username=None, email=None, password=None, **extra_fields):
        pass

class User(AbstractBaseUser, PermissionsMixin):
     """
     #doesnt use UUID, had to be changed to work with DB
     The user model that is created which inherits the AbstractBaseUser model of Django. Uses UUID as id, and email must be unique, and is optional.
     """
     username_validator = UnicodeUsernameValidator
     
     username = models.CharField(
        _('username'),
        max_length=150,
        unique=True,
        help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[username_validator],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
     )
     
     #id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
     email = models.EmailField(_('email address'), max_length=254, unique=True, null=True, blank=True)     
     is_participant = models.BooleanField(blank=True, default = False)
     is_researcher = models.BooleanField(blank=True, default = False)
     experiments = models.ManyToManyField(Experiment) #Create many to many relationship with User will only be relevant to researchers
     date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
     home_directory = models.CharField(max_length=150)
     objects = UserManager()
     
     EMAIL_FIELD = 'email'
     USERNAME_FIELD = 'username'
    
     is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
     )          
     
     class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        #had abstract = True
     def __str__(self):
         return self.username
     
     def clean(self):
        """
        Clean up blank fields to null
        """
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)
        
        if self.email == "":
            self.email = None
    
     def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)    

    

class Profile(models.Model):
    """
    Profile model which depends on user, has a cascading feature, if user is deleted, the profile will also be deleted.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    age = models.IntegerField(choices=AGE_CHOICES, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)  
    education = models.CharField(max_length=100, choices=EDUCATION_CHOICES, blank=True, null=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, null=True, blank=True)
    race = models.CharField(max_length=25, choices=RACE_CHOICES, null=True, blank=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    #To implement Encrypted fields... 
           # age = EncryptedIntegerField(choices=AGE_CHOICES, blank=True, null=True)
           # date_of_birth = EncryptedDateField(blank=True, null=True)  
           # education = EncryptedCharField(choices=EDUCATION_CHOICES, blank=True, null=True)
           # gender = EncryptedCharField(choices=GENDER_CHOICES, null=True, blank=True)
           # race = models.CharField(max_length=25, choices=RACE_CHOICES, null=True, blank=True)
           #  Disease1 = EncryptedTextField(null=True)
    
    def __str__(self):
        return '%s profile includes: age: %s, dateofBirth: %s'.format(self.user.username, self.user.age, self.user.date_of_birth)

class AnonUserCounter(models.Model):    
    """
        A simple counter that attaches to anon user
    """
    counter = models.IntegerField(blank=False, null=False)
    
    def save(self, *args, **kwargs):
        if (AnonUserCounter.objects.exists() and not self.pk):
            raise ValidationError('There can be only one AnonUserCounter instance')
        return super(AnonUserCounter, self).save(*args, **kwargs)
#No need to produce another class class called researcher or Participant because you can simply create a 
#boolean that differentiates each object
    
# class Researcher(User): #Inherits from User class, creates a table relating Researcher to User
#     """
#     Researcher model that has access to specific experiment data
#     """
#   #  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#   #  user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     experiment = models.ManyToManyField(Experiment)
#     
#     class Meta:
#         verbose_name = 'Researcher'
#         verbose_name_plural = 'Researchers'
#     
#     def _is_researcher(self):
#         return True
#     
# # class Participant(User): #Inherits from User class, creates a table relating Researcher to User
# #     """
# #     Participant model that will inherit from the User class
# #     """
# #     
# #     class Meta:
# #         verbose_name = 'Participant'
# #         verbose_name_plural = 'Participants'
# #         
# #     def _is_participant(self):
# #         return True
    
    
    
    
    
    
    
    
    
    
    
