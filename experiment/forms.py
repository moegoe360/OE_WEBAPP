from django import forms
from .models import Experiment, Attachment
from multiupload.fields import MultiFileField

class UploadForm(forms.Form):
    files =  MultiFileField(min_num=0, max_num=3, max_file_size=1024*1024*5, required=False)
      
class ExperimentForm(forms.ModelForm):
     class Meta:
        model = Experiment
        fields = ('name', 'description')
        
     files =  MultiFileField(min_num=0, max_num=3, max_file_size=1024*1024*5, required=False)

class ExperimentFormBasic(forms.ModelForm):
     class Meta:
        model = Experiment
        fields = ('name', 'description', 'is_Published')
        
  
#ExperimentFormSet = forms.inlineformset_factory(Experiment, Attachment)
                       
#      def clean_name(self):
#         name = self.cleaned_data['name']
#         valid_extensions = ['css', 'js', 'html']
#         print(name.rsplit('.', 1))
#         extension = name.rsplit('.', 1)[1].lower()
#         if extension not in valid_extensions:
#             raise forms.ValidationError('The given file isn\'t a text file')
#         return name
    
#      def save(self, commit=True):
#         instance = super(ExperimentForm, self).save(commit)
#         for each in self.cleaned_data['files']:
#             Attachment.objects.create(file=each, experiment=instance)
# 
#         return instance
#     
#      def save(self, commit=False):
#        instance = super(ExperimentForm, self).save(commit)
#        for each in self.cleaned_data['files']:
#            Attachment.objects.create(file=each)
#  
#        return instance
