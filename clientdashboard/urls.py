"""clientdashboard URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf.urls import include, url
from .views import index,product,cart,myindex
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$',index,name='index'),
    #url('product/',product,name='product'),
    url('cart/',cart,name='cart'),
    path('myindex/<my_id>/',myindex, name='myindex'),
    path('product/<my_product>/',product, name='product'),

]
