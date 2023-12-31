"""
URL configuration for setup project.

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
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from  App_Register import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'), # Home
    path('accounts/', include('django.contrib.auth.urls'), name = 'accounts'), # Login System
    path('List-User/', views.liste, name = 'list'), # Listing
    path('Form/', views.create, name = 'form'), # Creating
    path('List-User/User/<int:id>/', views.read, name = 'user'), # Reading
    path('List-User/User/Edit/<int:id>/', views.update, name= 'edit'), # Updating
    path('List-User/Remove/<int:id>/', views.remove, name= 'remove'), # Deleting
]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
