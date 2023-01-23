"""Product_API URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from app1.views import *
from app1 import views
from django.urls import re_path as url


urlpatterns = [
    path('admin/', admin.site.urls),
    path('upload_file', views.simple_upload),
    url(r'^api/prod/$', views.product_list),
    # url(r'^api/prod/$', views.ProdtList.as_view()),
    url(r'^api/products/(?P<pk>[0-9]+)/$', views.product_api),

]
