from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from django.core.urlresolvers import reverse
    
def user_directory_path(instance, filename):
     # file will be uploaded to experiments/uploads/researcher_<id>/<filename>
     return 'experiment/uploads/researcher_{0}/{1}.txt'.format(instance.owner, instance.name)
 
class Experiment(models.Model):
     date_uploaded = models.DateTimeField(_('date uploaded'), default=timezone.now) #rename to date_uploaded
     name = models.CharField(_("Experiment Name"), unique=True, max_length=100, null=False, blank = False)
     file = models.FileField(upload_to=user_directory_path, null=True, blank=True) 
     js_Code = models.TextField(blank=True, null=True)
     js_Code_Header = models.TextField(_("Any code for the header"), blank=True, null=True)
     is_Published = models.BooleanField(_("Published"), default=False)
     description = models.TextField(max_length=500, blank=True, null=True)
     created_By = models.CharField(max_length=50)
     
     def __str__(self):
         return self.name
     
     def get_absolute_url(self):
         return reverse("experiment:exp_detail", kwargs={'pk':self.pk})
         
     
