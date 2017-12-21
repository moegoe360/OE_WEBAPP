from django.shortcuts import render
from django.views.generic import (View, CreateView, UpdateView, DeleteView, DetailView, ListView, TemplateView)
# Create your views here.
from .models import *
from django.http.response import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse
from django.http import Http404
from django.utils.decorators import method_decorator


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

def belongsToResearcher(researcher, expID):
    """
        Checks if experiment belongs to researcher
    """
    try:
        researcher.experiments.get(id=expID)
        return True
    except:
        return False
            
class ExperimentDetailView(DetailView):
    """
        Using Django's generic DetailView which displays the detail(js code, data published, etc) of an experiment
    """
    context_object_name = 'experiment'
    model = Experiment
     
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
    fields = ('name', 'description', 'js_Code_Header', 'js_Code')
    model = Experiment
    success_url = reverse_lazy("experiment:exp_list")
     
    def form_valid(self, form):
        print("----====== ---======---- TESTING DEBUGGING ----====== ----======----")
        print("CheckPoint")
     
        print("----====== ---======---- ENDING DEBUGGING ----====== ----======----")
             
        exp = form.save(commit=False)
        exp.created_By = self.request.user.username
        exp.save()
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
        fields = ('name','description','js_Code_Header', 'js_Code', 'is_Published')
        model = Experiment
         
        @method_decorator(login_required)
        def dispatch(self, *args, **kwargs):
            if self.request.user.is_researcher and belongsToResearcher(self.request.user, DetailView.get_object(self).id):
                 return super(ExperimentUpdateView, self).dispatch(*args, **kwargs)
            else:
                return HttpResponse(Http404("You are not a researcher or experiment does not belong to you"))
         
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

