"""OE_Platform URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

# from wagtail.wagtailadmin import urls as wagtailadmin_urls
# from wagtail.wagtaildocs import urls as wagtaildocs_urls
# from wagtail.wagtailcore import urls as wagtail_urls
from django.conf.urls import *
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
from . import views
#from django.conf import settings


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.HomePage.as_view(), name='home'),
    url(r'^account/', include('account.urls', namespace='account')),
    url(r'^account/', include('django.contrib.auth.urls')),
    url(r'^experiment/', include('experiment.urls', namespace='experiment')),
    
#     url(r'^cms/', include(wagtailadmin_urls)),
#     url(r'^documents/', include(wagtaildocs_urls)),
#     url(r'^pages/', include(wagtail_urls)),
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)