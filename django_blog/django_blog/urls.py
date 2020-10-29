"""django_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView


urlpatterns = [
    path('admin/', admin.site.urls),
]
# Use include() to add paths from the catalog application 
from django.urls import include

urlpatterns += [
    path('about/', include('about.urls')),
]

urlpatterns += [
   path('blog/', include('blog.urls')),

]
#urlpatterns += [
 #  path('CV/', include('CV.urls')),

#]

urlpatterns += [
   path('E4/', include('E4.urls')),

]

urlpatterns += [
   path('E6/', include('E6.urls')),

]

urlpatterns += [
   path('veilletechno/', include('veilletechno.urls')),

]




#Add URL maps to redirect the base URL to our application
#from django.views.generic import RedirectView
urlpatterns += [
    path('', RedirectView.as_view(url='about/', permanent=True)),
]
# Use static() to add url mapping to serve static files during development (only)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
