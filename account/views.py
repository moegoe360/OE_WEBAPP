from django.http import HttpResponse
# from django.contrib.auth.views import LoginView
from django.shortcuts import render
from . import forms
# import datetime
from django.contrib import messages
# from uuid import UUID
# from experiment.models import Experiment
# from django.http.response import HttpResponseRedirect
#from django.urls.base import reverse, reverse_lazy
from django.core.urlresolvers import reverse_lazy
from .models import Profile, User
from django.http import Http404


from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth import authenticate, get_user, login
from django.views import generic
import os
from OE_Platform.settings import MEDIA_ROOT

  
def researcher_create_directory_path(instance): #May not need this method
     # file will be uploaded to /uploads/researcher_<id>/<experiment>/
     hdr = "uploads/researcher_{0}".format(instance.username)
     adr = os.path.join(MEDIA_ROOT, hdr)
     instance.home_directory = hdr 
     os.mkdir(adr)          
 
class RegisterAccount(generic.CreateView):
     """
         view method that registers a user if registration formed is filled out. Saves user as a participant or researcher depending on which url path is accessed.
     """
     form_class = forms.UserCreateForm
     success_url = reverse_lazy('account:register_done')
     template_name = 'account/registration/register.html'
      
     def form_valid(self, form):
         #Create a new user object but avoid saving it yet
         new_user = form.save(commit=False)
         #Set the chosen password_change
         new_user.set_password(form.cleaned_data['password1']) #set_password handles encryption for safety purposes
          #creates participant or researcher based on URL
         if self.request.path == "/account/register/":
                 #Identify user with participant
                 new_user.is_participant = True
                 #Save the User object
                 new_user.save()
                 #Create the user profile
                 profile = Profile.objects.create(user=new_user)
                 return super(RegisterAccount, self).form_valid(form)
         elif self.request.path == "/account/researcher/register/":
                 new_user.is_researcher = True
                 researcher_create_directory_path(new_user)
                 new_user.save()
                 return super(RegisterAccount, self).form_valid(form)

class RegisterAccountDoneView(generic.TemplateView):
     """
        A template view that displays register_done.html
     """
     template_name = 'account/registration/register_done.html'
 


class LoggedOutView(generic.TemplateView):
     """
         A template view that displays logged_out.html
     """
     template_name = 'account/logged_out.html'
     
@login_required
def dashboard(request): 
     """
         A view method that displays dashboard.html when user is logged in and passes a 'section' variable as 'dashboard'
     """
     return render(request, 'account/dashboard.html', {'section': 'dashboard'})
 
@login_required
def edit(request):
    """
        A view method that saves the changed data on the user profile or participant profile.
    """
    if request.method == 'POST':
        user_form = forms.UserEditForm(instance=request.user, data=request.POST)
        #profile_form
        if (request.user.is_participant):
            profile_form = forms.ProfileEditForm(instance=request.user.profile, data=request.POST)
         
        if not (user_form.has_changed() or profile_form.has_changed()): 
            messages.info(request, 'There was no changes done on the profile ')
        elif user_form.is_valid() and profile_form.is_valid():  
            #To do-> Add code that checks date and compares it to age, give an error if they dont match
            user_form.save()
            if (request.user.is_participant):
                profile_form.save()
            messages.success(request, 'Profile updated successfuly')
         #if not user_form.data['date_of_birth']:
          #      born = user_form.data['date_of_birth']
           #     today = datetime.datetime.now()
            #    get_user(request).Profile.age = today.year - born.year - ((today.month, today.day) < (born.month, born.day))
          
        else:
            messages.error(request, 'Error updating your profile')
    else:
        user_form = forms.UserEditForm(instance=request.user)
        if (request.user.is_participant):
            profile_form = forms.ProfileEditForm(instance=request.user.profile)
     
    if (request.user.is_participant):
        return render(request, 'account/edit.html', {'user_form': user_form, 'profile_form': profile_form})
    else:
        return render(request, 'account/edit.html', {'user_form': user_form})

 
@login_required
def accountRemoval(request):
    """
        A view method that allows the user to completely remove their account.
    """
    if 'remove_profile' in request.POST:
       # messages.info(request, 'You clicked button 1')
       pass
    elif 'remove_all' in request.POST:
       # messages.info(request, 'You clicked button 2')
       instance = get_user(request)
       instance.delete()
       return render(request, 'account/logged_out.html')
         
    return render(request, 'account/account_remove.html')
 
 #CODE USED FOR DJANGO 2.11 - cannot use because needed to downgrade code
 
 # class UserLoginView(LoginView):
#     template_name = 'account/login.html'

# class DashboardView(generic.TemplateView):
#     template_name = 'account/dashboard.html'

# class AccountUpdateView(generic.UpdateView):
#         #model = Profile
#         model = User
#         form_class = forms.ProfileEditForm
#         second_form_class = forms.UserEditForm
#         #second_form_class = forms.UserEditForm
#         template_name = 'account/edit.html'
#          
#         def get_success_url(self):
#             return reverse_lazy('account:edit')
#  
# #         def get_context_data(self, **kwargs):
# #             context = super(AccountUpdateView, self).get_context_data(**kwargs)
# #             context['second_model'] = SecondModel.objects.get(id=1) #whatever you would like
# # #             return context
#  
# #         def get(self, request, *args, **kwargs):
# #             super(AccountUpdateView, self).get(request, *args, **kwargs)
# #             form = self.form_class
# #             form1 = self.second_form_class
# #             return self.render_to_response(self.get_context_data(object=self.object, form=form, form1=form1))
#  
#         def get_object(self):
#             return self.request.user.profile
        
#         def get_context_data(self, **kwargs):
#              context = super(AccountUpdateView, self).get_context_data(**kwargs)
#              context['form'] = self.form_class(self.request.GET, instance=self.request.user)
#             # context['form1'] = self.second_form_class(self.request.GET)
#              return context
#          
#         @method_decorator(login_required)
#         def dispatch(self, *args, **kwargs):
#              if self.request.user.is_participant:
#                   return super(AccountUpdateView, self).dispatch(*args, **kwargs)
#              else:
#                  return HttpResponse(Http404("You are not a participant"))
# 
#         def form_valid(self, form, form1):
#             if not (form.has_changed() or form1.has_changed()):
#                 messages.info(self.request, 'there was no change done on the profile ')
#             elif form.is_valid() and form1.is_valid():
#     #To do-> Add code that checks date and compares it to age, give an error if they dont match
#                 form.save()
#                 form1.save()
#                 messages.success(self.request, 'Profile updated successfuly')
#             else:
#                 messages.error(self.request, "Error updating your profile")
#             return super(AccountUpdateView, self).form_valid(form)
      # def edit(request):
#     if request.method == 'POST':
#         user_form = UserEditForm(instance=request.user, data=request.POST)
#         profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST)
#         
#         if not (user_form.has_changed() or profile_form.has_changed()): 
#             messages.info(request, 'There was no changes done on the profile ')
#         elif user_form.is_valid() and profile_form.is_valid():  
#             user_form.save()
#             profile_form.save()
#             messages.success(request, 'Profile updated successfuly')
#          #if not user_form.data['date_of_birth']:
#           #      born = user_form.data['date_of_birth']
#            #     today = datetime.datetime.now()
#             #    get_user(request).Profile.age = today.year - born.year - ((today.month, today.day) < (born.month, born.day))
#          
#         else:
#             messages.error(request, 'Error updating your profile')
#     else:
#         user_form = UserEditForm(instance=request.user)
#         profile_form = ProfileEditForm(instance=request.user.profile)
#     
#     return render(re  
    
# OBSOLETE CODE THAT WON'T BE USED DUE TO UPDATED DJANGO TO 1.11

#Used a loginview premade by django auth

# def user_login(request):
#     if request.method == 'POST':
#         form = forms.LoginForm(request.POST)
#         if form.is_valid():
#                cd = form.cleaned_data #Normalizes the form to be outputted into python properly, ex. datetime.date
#                user = authenticate(username=cd['username'],
#                                    password=cd['password'])
#                if user is not None:
#                    if user.is_active:
#                        login(request, user)
#                        return render(request, 'account/dashboard.html')
#                           
#                    else:
#                        return HttpResponse('Disabled account')  
#                else:
#                    return HttpResponse('Invalid login')
#     else:
#          form = forms.LoginForm()
#     return render(request, 'account/login.html', {'form': form})

# USED TEMPLATE VIEW INSTEAD
# def register(request):
#     if request.method == 'POST':
#         user_form = UserRegistrationForm(request.POST)
#         if user_form.is_valid():
#             #Create a new user object but avoid saving it yet
#             new_user = user_form.save(commit=False)
#             #Set the chosen password_change
#             new_user.set_password(user_form.cleaned_data['password']) #set_password handles encryption for safety purposes
#             
#             #creates participant or researcher based on URL
#             if request.path == "/account/register/":
#                 #Identify user with participant
#                 new_user.is_participant = True
#                 #Save the User object
#                 new_user.save()
#                 #Create the user profile
#                 profile = Profile.objects.create(user=new_user)
#             elif request.path == "/account/researcher/register/":
#                 new_user.is_researcher = True
#                 new_user.save()
#             return render(request, 'account/register_done.html',{'new_user' : new_user})
#     else:
#         user_form = UserRegistrationForm()
#     return render(request, 'account/register.html', {'user_form': user_form})


# 

#         