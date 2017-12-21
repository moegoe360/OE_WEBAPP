from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from django.core.urlresolvers import reverse
    
def user_directory_path(instance, filename): #May not need this method
     # file will be uploaded to experiments/uploads/researcher_<id>/<filename>
     return 'experiment/uploads/researcher_{0}/{1}.txt'.format(instance.owner, instance.name)

class Experiment(models.Model):
     """
        Builds the experiment model that will store javascript code to display to their corresponding experiment page.
     """
     date_uploaded = models.DateTimeField(_('date uploaded'), default=timezone.now) 
     name = models.CharField(_("Experiment Name"), unique=True, max_length=100, null=False, blank = False)
    # file = models.FileField(upload_to=user_directory_path, null=True, blank=True) #May not need this...
     js_Code = models.TextField(blank=True, null=True)
     js_Code_Header = models.TextField(_("Any code for the header"), blank=True, null=True) # The JS code entered in the header of the HTML
     is_Published = models.BooleanField(_("Published"), default=False)
     description = models.TextField(max_length=500, blank=True, null=True)
     created_By = models.CharField(max_length=50)
     
     def __str__(self):
         """
             Returns the name of the experiment in string
         """    
         return self.name
     
     def get_absolute_url(self):
         return reverse("experiment:exp_detail", kwargs={'pk':self.pk})
     
class Question(models.Model):
    """
        The model that holds each question of the form used by each experiment
    """
    question = models.CharField(max_length=128)
    experiment = models.ManyToManyField(Experiment)

class Answer(models.Model):
    """
        The model that holds the answers related to the questions
    """
    question = models.ForeignKey(Question)
    answer = models.CharField(max_length=20)
    
         
     
