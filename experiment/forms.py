from django import forms
from .models import Experiment

# class UploadFileForm(forms.ModelForm):
#      class Meta:
#         model = Experiment
#         fields = ('name', 'description','file', 'js_Code')
        
#     def clean_name(self):
#         name = self.cleaned_data['name']
#         valid_extensions = ['txt']
#         extension = name.rsplit('.', 1)[1].lower()
#         if extension not in valid_extensions:
#             raise forms.ValidationError('The given file isn\'t a text file')
#         return name