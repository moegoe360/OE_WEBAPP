from django.shortcuts import render
from django.views.generic import (View, CreateView, UpdateView, DeleteView, DetailView, ListView, TemplateView)
# Create your views here.
from .models import *
from .forms import *
from django.shortcuts import get_object_or_404
from OE_Platform.settings import MEDIA_ROOT
from OE_Platform.mixins import AjaxableResponseMixin
from django.views.generic.base import TemplateResponseMixin
from django.views.generic.edit import FormMixin, BaseCreateView
from django.views.generic.list import BaseListView
from django.http.response import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse
from django.http import Http404
from django.utils.decorators import method_decorator
import os
import json
from OE_Platform.settings import MEDIA_ROOT

from psycopg2 import sql
import psycopg2
from psycopg2.extensions import AsIs
from django.db import connection

       
def experiment_create_directory_path(user, experiment):
     # folder will be created on experiment creation media/uploads/researcher_<id>/<experiment>/
     dr = os.path.join(user.home_directory, experiment.name) 
     experiment.home_directory = dr
     os.mkdir(os.path.join(MEDIA_ROOT, dr))
     
def belongsToResearcher(researcher, expID):
    """
        Checks if object belongs to researcher, if num==0, checks experiment, if num==1 checks attachment
    """
    try:
        researcher.experiments.get(id=expID)
        return True
    except:
        return False
    
def multipleFilesUpload(form, exp, instance):
    for each in form.cleaned_data['files']:
        Attachment.objects.create(file=each, experiment=exp)
        
class FormAndListView(BaseCreateView, BaseListView, TemplateResponseMixin):
    def get(self, request, *args, **kwargs):
        formView = BaseCreateView.get(self, request, *args, **kwargs)
        listView = BaseListView.get(self, request, *args, **kwargs)
        formData = formView.context_data['form']
        listData = listView.context_data['object_list']
        return render_to_response('textfrompdf/index.html', {'form' : formData, 'all_PDF' : listData}, context_instance=RequestContext(request))
    
class FormListView(FormMixin, ListView):
    """
        Helps produce a form and list in one view
    """
    def get(self, request, *args, **kwargs):
        # From ProcessFormMixin
        form_class = self.get_form_class()
        self.form = self.get_form(form_class)

        # From BaseListView
        self.object_list = self.get_queryset()
        allow_empty = self.get_allow_empty()
        if not allow_empty and len(self.object_list) == 0:
            raise Http404(_(u"Empty list and '%(class_name)s.allow_empty' is False.")
                          % {'class_name': self.__class__.__name__})

        context = self.get_context_data(object_list=self.object_list, form=self.form)
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        return self.get(request, *args, **kwargs)
    
class ExperimentListView(ListView):
    """
        Using Django's generic ListView which displays all experiments in list format
    """
    context_object_name = 'experiments'
    model = Experiment
    
    
#     def researcherPortal(request):  
#             return render(request, 'account/experiment_list.html', {'section': 'experiment_list'})
   
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        if self.request.user.is_researcher:
            return super(ExperimentListView, self).dispatch(*args, **kwargs)
        else:
            return HttpResponse(Http404("You are not a researcher"))
    
class ExperimentDetailView(DetailView):
    """
        Using Django's generic DetailView which displays the detail(js code, data published, etc) of an experiment
    """
    context_object_name = 'experiment'
    model = Experiment
    
    def get_context_data(self, **kwargs):
        context = super(ExperimentDetailView, self).get_context_data(**kwargs)
        context['attachments'] = DetailView.get_object(self).attachment_set.all() #get all attachments of detailview object (experiment)
        return context   
          
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        if self.request.user.is_researcher and belongsToResearcher(self.request.user, DetailView.get_object(self).id):
            return super(ExperimentDetailView, self).dispatch(*args, **kwargs)
        else:
            return HttpResponse(Http404("You are not a researcher or experiment does not belong to you"))
        
class ExperimentCreateView(CreateView):
    """
        Using Django's generic CreateView which produces a form that will help a researcher produce an experiment. Once form is filled out, experiment model is saved in database.
    """
    #fields = ('name', 'description')
    model = Experiment
    form_class = ExperimentForm
    template_name = 'Experiment/experiment_form.html'
    success_url = reverse_lazy("experiment:exp_list")
     
    def form_valid(self, form):
        print("----====== ---======---- TESTING DEBUGGING ----====== ----======----")
        print("CheckPoint")
     
        print("----====== ---======---- ENDING DEBUGGING ----====== ----======----")
             
        exp = form.save(commit=False)
        exp.created_By = self.request.user.username
        experiment_create_directory_path(self.request.user, exp)
        exp.save()
        multipleFilesUpload(form, exp, self.request) # use this later 
        self.request.user.experiments.add(exp)
        self.request.user.save() 
        messages.success(self.request, 'file added successfully')
        print(exp.get_absolute_url())
         
        return super(ExperimentCreateView, self).form_valid(form)
     
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        if self.request.user.is_researcher:
            return super(ExperimentCreateView, self).dispatch(*args, **kwargs)
        else:
            return HttpResponse(Http404("You are not a researcher"))
    
class ExperimentUpdateView(UpdateView):
        """
            Using Django's generic UpdateView which produces a form that will help researchers to edit the experiment detail.
        """
        model = Experiment
        form_class = ExperimentFormBasic
        #fields = ['name', 'description']
        template_name = 'Experiment/experiment_update.html'
#         def get_object(self, queryset=None):
#             return get_object_or_json404(Experiment, pk=self.kwargs['pk'])
        
#         def get_context_data(self, **kwargs):
#             context = super(ExperimentUpdateView, self).get_context_data(**kwargs)
#             context['attachments'] = UpdateView.get_object(self).attachment_set.all() #UpdateView.get_object(self).attachment_set.all()
#             #print(context['attachments'])
#             return context 
#         
#         def post(self, request, *args, **kwargs):
#             #form = self.form_class(request.POST)
#             super(ExperimentUpdateView, self).post(request, *args, **kwargs)
#             delete_btn_clicked = 'file_delete' in request.POST
#             form = self.form_class(request.POST)
#             if not (form.is_valid()): 
#                 #messages.info(request, 'There was no changes done on the profile ')
#                 if 'file_delete' in request.POST:
#                     #id = request.POST['id']
#                      
#                    # print("Id is:" + id)
#                    # print("request:");  
#                     #print(request)
#                     #print("request POST id");  
#                     ids = request.POST.getlist('id')
#                     #print(ids)
#                     #print("object attachment");  
#                     for i in ids:
#                         print(i)
#                         #Attachment.objects.get(id=i).fullDelete()
#                         #Attachment.objects.get(id=i).delete()
#                         
#             return render(request, self.template_name, {'form': form})
#            
#             #elif form.is_valid():
#               #  return HttpResponseRedirect('/success/')
#          
#             #return render(request, self.template_name, {'form': form})
#           
       
        @method_decorator(login_required)
        def dispatch(self, *args, **kwargs):
            if self.request.user.is_researcher and belongsToResearcher(self.request.user, UpdateView.get_object(self).id):
                 return super(ExperimentUpdateView, self).dispatch(*args, **kwargs)
            else:
                return HttpResponse(Http404("You are not a researcher or experiment does not belong to you"))
            
class FileDeleteView(DeleteView):
        """
            Using Django's generic DeleteView to remove 
        """
        model = Attachment
        
        def get_context_data(self, **kwargs):
            context = super(DeleteView, self).get_context_data(**kwargs)
            context['epk'] = self.kwargs.get('epk', '')
            return context 
         
        def delete(self, request, *args, **kwargs):
            print("got deleted")
            obj = self.get_object()
            print(obj)
            obj.fullDelete()
            obj.delete()
            k = self.kwargs.get('epk', '')
            messages.success(self.request, 'file deleted successfully')
            return HttpResponseRedirect(reverse('experiment:file_list', args=[k]))

class FileListView(CreateView): #FormAndListView   FormListView
    """
    
    """
    model = Attachment
    fields = ['file']
    template_name = "experiment/attachment_list.html"
    
    def get_success_url(self):
        return reverse('experiment:file_list', args=[self.kwargs.get('epk', '')])   
   
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        if self.request.user.is_researcher:
             return super(FileListView, self).dispatch(*args, **kwargs)
        else:
            return HttpResponse(Http404("You are not a researcher or file does not belong to you"))
#     def get_queryset(self):
#         return Experiment.objects.get(id=self.kwargs.get('epk', '')).attachment_set.all()
       
    def form_valid(self, form):
        if ('upload_file' in self.request.POST):
                
                form.instance.experiment = Experiment.objects.get(id=self.kwargs.get('epk', ''))
           
           # user_form = forms.(data=request.POST)
#             for each in form.cleaned_data['file']:
#                # Attachment.objects.create(file=each)
#                 Attachment.objects.create(file=each, experiment=exp)
#                 instance.user.experiments.add(exp)
#                 instance.user.save() 
        return super(FileListView, self).form_valid(form)
#     def post(self, form, epk):
#         print("test1")
#         if ('upload_file' in self.request.POST):
#             print("check2")
#             
#             print(form)
#             print(self.context)
#             k = self.kwargs.get('epk', '')
#             exp = Experiment.objects.get(id=k)
#             messages.success(self.request, 'file added successfully')
#         return HttpResponseRedirect(reverse('experiment:file_list', args=[epk]))  
        
    def get_context_data(self, **kwargs):
        context = super(FileListView, self).get_context_data(**kwargs)
        context['epk'] = self.kwargs.get('epk', '')
        context['attachments'] = Experiment.objects.get(id=self.kwargs.get('epk', '')).attachment_set.all()
        return context 
#     
#     def form_valid(self, form):
#         print("form is valid")
#         return super(RegisterAccount, self).form_valid(form)

    
    
    
#     def get_queryset(self):
#         self.experiment = get_object_or_404(Experiment, name=self.args[0])
#         return Attachment.objects.filter(Experiment=self.experiment)      
#     def post(self, request, *args, **kwargs):
#         if "delete" in request.POST:
#             print("delete worked")
#             print(self.request)
#             print(dir(self.request))
#             #id = request.POST['id']
# #                      
# #                    # print("Id is:" + id)
# #                    # print("request:");  
# #                     #print(request)
# #                     #print("request POST id");  
# #                     ids = request.POST.getlist('id')
# #                     #print(ids)
# #                     #print("object attachment");  
# #                     for i in ids:
# #                         print(i)
# #                         #Attachment.objects.get(id=i).fullDelete()
# #                         #Attachment.objects.get(id=i).delete()
#         if "upload" in request.POST:
#             pass
#         return render(request, "experiment/attachment_list.html")

class ExperimentDeleteView(DeleteView):
        """
            Using Django's generic DeleteView which displays a simple delete page for the experiment model
        """
        model = Experiment
        success_url = reverse_lazy("experiment:exp_list") #reverse_lazy used because it waits for all the code to run before running
         
        @method_decorator(login_required)
        def dispatch(self, *args, **kwargs):
            if self.request.user.is_researcher and belongsToResearcher(self.request.user, DetailView.get_object(self).id):
                 return super(ExperimentDeleteView, self).dispatch(*args, **kwargs)
            else:
                return HttpResponse(Http404("You are not a researcher or experiment does not belong to you"))
            
        def delete(self, request, *args, **kwargs):
            print("Experiment deleted")
            obj = self.get_object()
            a = obj.attachment_set.all()
            for i in a:     # Deletes each attachment object and it's files
                i.fullDelete()
                i.delete()
            os.rmdir(os.path.join('media', obj.home_directory))
            obj.delete()
            messages.success(self.request, 'Experiment deleted successfully')
            return HttpResponseRedirect(reverse('experiment:exp_list'))
                 
class ExperimentPublicListView(ListView):
    """
        Using Django's generic ListView to display a list of the experiments that will be displayed to all users. Renders experiment_list_public.html.
    """
    context_object_name = 'experiments'
    model = Experiment
    template_name = "experiment/experiment_list_public.html"
     
     
class ExperimentPublicTest(DetailView):
    """
        Using Django's generic DetailView which displays basic experiment detail and will render experiment.html
    """
    context_object_name = 'experiment'
    model = Experiment
    template_name = "experiment/experiment.html"
    
    def get_context_data(self, **kwargs):
        context = super(ExperimentPublicTest, self).get_context_data(**kwargs)
        attachments = self.get_object().attachment_set.all()
        context['htmlFile'] = [x for x in attachments if 'html' in x.filename()][0]
#         for x in attachments:
#             if ('html' in x.filename()):
                
       # print([x for x in attachments if 'html' in x][0])
       # htmlFile = 
        
        return context 
    
def tableExist(table_name):
    try:
        cursor.execute("SELECT to_regclass(%s)",table_name)
        if cursor.fetchone()[0]:
            return 1
        else:
            return 0
    except:
        print("error checking if table exists")

def createTable(table_name, sql):
    cursor = connection.cursor()
    #check if table exists
    if tableExist(table_name):
        print("table already exists")
    else:
        try:
            #sql should be created from the output data
            cursor.execute(sql, (AsIs(table_name),)) #creates the table
            print("table created")
            cursor.close()
            connection.commit() #commit the changes
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if connection is not None:
                connection.close()
            
def insertTable(table_name, data):
    cursor = connection.cursor()
    sd = 0
    if data[0] == "[":
        keys = data[0].keys() #data must be predictable, will it always be a json?? prob not
        columns = ",".join(data[0].keys())

    else:
       keys = data.keys() #assuming data is dict
       columns = ",".join(data.keys())
       sd = 1
    #values = ",".join("'" + v + "'" if type(v) is str else str(v) for v in data.values())
    #sql = "INSERT into %s %s"
    #Method that is faster than executemany apparently...
    #maybe at the end of the experiment the number of %s should be added like so.
    #args_str = ','.join(cur.mogrify("(%s,%s,%s,%s,%s,%s,%s,%s,%s)", x) for x in tup)
    #cur.execute("INSERT INTO table VALUES " + args_str) 
    #count how many columns for insertion...
    qr = ','.join(['%s'] * len(data[0])) #adds multiple %s in a string

    try:
        query = cursor.mogrify("INSERT into %s (%s) VALUES (%s);", (AsIs(table_name),AsIs(columns), AsIs(qr))).decode()
        vals = []
        if sd:
            for x,y in data.items:
                vals.append(tuple(y.values()))
            cursor.execute(query, vals)   
        else:    
            for x in data:
                vals.append(tuple(x.values()))
            cursor.executemany(query, vals)
       # cursor.execute(sql, , AsIs(columns), AsIs(values))) #creates the table
        print("Values inserted")
        cursor.close()
        connection.commit() #commit the changes
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()
    
    
def PostData(request): #Runs backend stuff
    print("POST DATA is: " + str(request.POST))
    #get userid //deal with anonymous users later. but for now have a system for logged in users
    uID = request.user.id #get user ID
    print("userID: " + str(uID))
    #get experiment id
    eID = request.POST['expID'] #get experiment ID
    print("expID: " + str(eID))
    a = request.POST
    data = request.POST['data']
    print("data is: " + str(data))
    # Data received...
    #table name will be... exp+expID_userID...anonymous users have to have their own ID
    table_name = "exp" + str(eID) + "_" + str(uID) #we can adjust the table name to account for different schema...do we need it?
    #create function to validate table name, for safety purposes
    #tableNameValidation(table_name)
    print(table_name)
    createTable(table_name, query)
    #insert into table
    data = json.loads(data)
    insertTable(table_name, data)
    
    return HttpResponse(a)
    







