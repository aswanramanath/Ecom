"""
URL configuration for ecommerse project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from ecom import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Home.as_view(),name='home_view'),
    path('reg',views.Useregisterview.as_view(),name='reg'),
    path('login',views.UserLogin.as_view(),name='Userlogin'),
    path('logout',views.Logout.as_view(),name='LOGOUT'),
    path('details/<int:id>',views.Productdetails.as_view(),name='productdetails'),
    path('addcart/<int:id>',views.Addtocart.as_view(),name='addcart_1'),
    path('showcart/',views.Cartproduct.as_view(),name='crtpr'),
    path('order/<int:cart>',views.Plcaeorder_view.as_view(),name='Order'),
    path('delete/<int:id>',views.DeleteCart.as_view(),name='Deletecart')



]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT )

