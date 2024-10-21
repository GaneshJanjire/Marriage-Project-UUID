"""
URL configuration for Matrimony_Proj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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


urlpatterns = [
    path('admin/', admin.site.urls),
    path('UserProfile_App/', include('UserProfile_app.urls')),

    path('ContactUs_App/', include('ContactUs_App.urls')),

    path('HoroscopeDetails_App/', include('HoroscopeDetails_App.urls')),

    path('EducationDetails_App/', include('EducationDetails_App.urls')),

    path('Familydetails_App/', include('Familydetails_App.urls')),

    path('PartnerPreferenceDetails_App/', include('PartnerPreferenceDetails_App.urls')),

    path('Habbits_Interest_App/', include('Habbits_Interest_App.urls')),
]
