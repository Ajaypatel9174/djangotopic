"""
URL configuration for project project.

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
from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('register/',views.register,name='register'),
    path('registerdata/',views.registerdata,name='registerdata'),
    path('login/',views.login,name='login'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('dashboard/query/<int:pk>/',views.query,name='query'),
    path('querydata/',views.querydata,name='querydata'),
    path('showquery/<int:pk>/',views.showquery,name='showquery'),
    path('edit/<int:pk>/<int:pke>/',views.edit,name='edit'),
    path('update/<int:pk>/<int:pke>/',views.update,name='update'),
    path('delete/<int:pk>/<int:pke>/',views.delete,name='delete'),
    path('logout/',views.logout,name='logout'),
    path('login/dasboard/search',views.Search,name='Search')
    

    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
