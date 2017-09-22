from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
import uuid
from account.choices import *
from experiment.models import Experiment
#from django.forms import extras
#from django.forms.widgets import SelectDateWidget

#from pgcrypto_expressions.fields import *
#from pgcrypto import *

#from fernet_fields import EncryptedTextField

# Create your models here.
class User(AbstractUser):
     """
     The user model that is created which inherits the AbstractUser model of Django. Uses UUID as id, and email must be unique, and is optional.
     """
     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
     #email = models.EmailField(_('email address'), max_length=254, unique=True, null=True, blank=True)     
     is_participant = models.BooleanField(blank=True, default = False)
     is_researcher = models.BooleanField(blank=True, default = False)
     experiments = models.ManyToManyField(Experiment) #Create many to many relationship with Use will only be relevant to researchers
                            
     def __str__(self):
         return self.username
     
     def clean(self):
        """
        Clean up blank fields to null
        """
        if self.email == "":
            self.email = None
    

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
    
    
    
    
    
    
    
    
    
    
    
