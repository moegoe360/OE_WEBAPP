from django.conf.urls import url
#from django.contrib.auth import views as auth_views
from OE_Platform import views as auth_views
from . import views 

app_name = "account"

urlpatterns = [
     url(r'^$', views.DashboardView.as_view(), name='dashboard'),
     url(r'^login/$', auth_views.LoginView.as_view(template_name='account/login.html'), name='login'),
     url(r'^logout/$', auth_views.LogoutView.as_view(template_name='account/logged_out.html'), name='logout'),    
     url(r'^register/$', views.RegisterAccount.as_view(), name='register'),
     url(r'^register_done/$', views.RegisterAccountDoneView.as_view(), name='register_done'),
#These following URLs will allow us to change passwords
     url(r'^password_change/$', auth_views.PasswordChangeView.as_view(template_name='account/registration/password_change_form.html'), name='password_change' ),
     url(r'^password-change/done/$', auth_views.PasswordChangeDoneView.as_view(template_name='account/registration/password_change_done.html'), name='password_change_done'),
#URLS for Restoring the password 
     url(r'^password-reset/$', auth_views.PasswordResetView.as_view(template_name='account/registration/password_reset_form.html'), name='password_reset'),
     url(r'^password-reset/done/$', auth_views.PasswordResetDoneView.as_view(template_name='account/registration/password_reset_done.html'), name='password_reset_done'),
     url(r'^password-reset/confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$', auth_views.PasswordResetConfirmView.as_view(template_name='account/registration/password_reset_confirm.html'), name='password_reset_confirm'),
     url(r'^password-reset/complete/$', auth_views.PasswordResetCompleteView.as_view(template_name='account/registration/password_reset_complete.html'), name='password_reset_complete'),

#Researcher URLS
#Create Account
     url(r'^researcher/register/$', views.RegisterAccount.as_view(), name='reseacher_register'),
     
    
     url(r'^edit/$', views.AccountUpdateView.as_view(), name='edit'),
    ]


# OBSOLETE CODE 
#     url(r'^logout/$', auth_views.logout, name='logout'),
#     url(r'^logout-then-login/$', auth_views.logout_then_login, name='logout_then_login'),
#     #These following URLs will allow us to change passwords
#     url(r'^password-change/$', auth_views.password_change, name='password_change'),
#     url(r'^password-change/done/$', auth_views.password_change_done, name='password_change_done'),
#     
#     #URLS for Restoring the password 
#     url(r'^password-reset/$', auth_views.password_reset, name='password_reset'),
#     url(r'^password-reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
#     url(r'^password-reset/confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$', auth_views.password_reset_confirm, name='password_reset_confirm'),
#     url(r'^password-reset/complete/$', auth_views.password_reset_complete, name='password_reset_complete'),
#     
#     #URL for user-participant creation
#     url(r'^register/$', views.register, name='register'),

#     
#     url(r'^edit/$', views.edit, name='edit'),
#     url(r'^user_remove/$', views.accountRemoval, name='account_remove'),
#     
#     #Researcher URLS
#         #Create Account
#     url(r'^researcher/register/$', views.register, name='reseacher_register'),
#         #researcher portal
