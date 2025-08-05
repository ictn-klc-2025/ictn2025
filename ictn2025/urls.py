"""
URL configuration for ictn2025 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", TemplateView.as_view(template_name="base.html"), name="base"),
    path("home", TemplateView.as_view(template_name="home.html"), name="home"),
    path("registration", TemplateView.as_view(template_name="registration.html"), name="registration"),
    path("speakers", TemplateView.as_view(template_name="speakers.html"), name="speakers"),
    path("sponsorship", TemplateView.as_view(template_name="sponsorship.html"), name="sponsorship"),
    path("publications", TemplateView.as_view(template_name="publications.html"), name="publications"),
    path("awards", TemplateView.as_view(template_name="awards.html"), name="awards"),
    path("organizers", TemplateView.as_view(template_name="organizers.html"), name="organizers"),
]



if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

