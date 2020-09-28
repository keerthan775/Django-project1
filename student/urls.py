"""student URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path,include
from db_insert import views as ins_view
from db_delete import views as del_view
from db_select import views as select_view
from db_update import views as update_view


urlpatterns = [
    path('admin/', admin.site.urls),
     path('dbinserthome',ins_view.home),
     path('dbdeletehome',del_view.home),
     path('dbinsert',ins_view.insert),
     path('dbdelete',del_view.dbdelete),
     path('dbselecthome',select_view.home),
     path('dbselect',select_view.dbselect),
     path('dbupdatehome',update_view.home),
     path('dbupdate',update_view.dbupdate),
]
