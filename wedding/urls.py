"""
URL configuration for wedding project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from wedding import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index_page , name='home'),
    path('about', views.about_page, name='about'),
    path('story', views.story_page, name='story'),
    path('gallery', views.gallery_page, name='gallery'),
    path('contact', views.contact_page, name='contact'),
    path('wedding-venues/', views.wedding_venues, name='wedding-venues'),
    path('api/',include('ourguardsnew.urls_api')),
]
if settings.DEBUG:
   urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
