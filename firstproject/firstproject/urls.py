"""
URL configuration for firstproject project.

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
from django.urls import path,re_path
from FristApp import views
from MultiViewsApp import views as v1


#from App1 import views
#from App2 import views

#Approch1
from App1 import views as v11
from App2 import views as v22

#Approch2
from App1.views import f11
from App2.views import f22

urlpatterns = [
    path('admin/', admin.site.urls),
    path('welcome/',views.display),
    path('welcome2/',views.show),
    path('hello/',views.hello),
    #MultiViewsApps-urls
    #MultiViewsApps as v1(alias to views.py)
    path('mrng/',v1.f1),
    path('aftr/',v1.f2),
    path('evng/',v1.f3),
    #Approch1-urls
    path('hello2/',v11.f11),
    path('datetime2/',v22.f22),
    #Approch2-urls
    path('hello3/',v11.f11),
    path('datetime3/',v22.f22),
    #mulitple-urls same-views-func & same-response
    path('fristdemo/',views.demo),
    path('seconddemo/',views.demo),
    path('thirddemo/',views.demo),
    
    
    
    #default-homepage
        re_path("^.*$",views.homepage),
    
]
