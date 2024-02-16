from django.shortcuts import render,redirect
from django.views import View
from ecom.forms import Useregister,LoginForm,cartForm,Orderform
# from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from ecom.models import Product,Carts,Order




class Home(View):
    def get(self,request,*args,**kwargs):
        data=Product.objects.all()
        return render(request,'index.html',{'data':data})


class Useregisterview(View):
    def get(self,request,*args,**kwargs):
        from1=Useregister()
        return render(request,'User_register.html',{'f1':from1})

    def post(self,request,*args,**kwargs):
        # name=request.POST['first_name']
        # lname=request.POST['last_name']
        # username=request.POST['username']
        # email=request.POST['email']
        # psw=request.POST['password']
        # data=User.objects.create(first_name=name,last_name=lname,username=username,email=email,password=psw)
        # return HttpResponse("<h1>DONE SUCESS FULLY BITCHHHHHHHHHHHHHH")

        form=Useregister(request.POST)
        if form.is_valid():
            User.objects.create_user(**form.cleaned_data)
            messages.success(request,'REGISTRION SUCESS FULL')
            return HttpResponse('SUCESS')
        else:
            messages.error(request,'Invalid')
            return redirect('home_view')
        

class UserLogin(View):
    def get(self,request,*args,**kwargs):
        login=LoginForm()
        return render(request,'userlogin.html',{"login":login})
    def post(self,request,*args,**kwargs):
# Create your views here.
         
        uname=request.POST.get('username')
        pasw=request.POST.get('password')
        data1=authenticate(request,username=uname,password=pasw)
        if data1: 
              login(request,data1)
              messages.success(request,'login scessfull')
              return redirect('home_view')
        else :
            
              messages.error(request,'UN SUCEESSFULL')
              return redirect('Userlogin')
        # data=LoginForm(request.POST)
        # if data.is_valid():
        #     uname=request.cleaned_data.get('username')
        #     pasw=request.POST.get('password')
        #     user=authenticate(request,username=uname,password=pasw)
        #     if user:
        #         login(request,user)
        #         messages.success(request,"LOGIN SUCESS")
        #         return redirect('home_view')
        #     else:
        #         messages.error(request,"un SUCESS")
        #         return redirect('Userlogin')


class Logout(View):
    def get(self,request,*args,**kwargs):

        logout(request)
        messages.success(request,"logout sucesss")
        return redirect('home_view')


class Productdetails(View):
    def get(self,request,*args,**kwargs):
     id=kwargs.get('id')
     data1=Product.objects.get(id=id)
     return render(request,'productdetails.html',{'product':data1})

class Addtocart(View):
    def get(self,request,*args,**kwargs):
        form=cartForm()
        id=kwargs.get('id')
        prd=Product.objects.get(id=id)
        return render(request,'addtocart.html',{'addcart':form,'product':prd})
    def post(self,request,*args,**kwargs):
        user=request.user
        id=kwargs.get('id')
        prd=Product.objects.get(id=id)
        qty=request.POST.get('quantity')
        Carts.objects.create(user=user,product=prd,quantity=qty)
        return redirect('home_view')
    
class Cartproduct(View):
    def get(self,request,*args,**kwargs):
         cart=Carts.objects.filter(user=request.user).exclude(status='order-placed')
         return render(request,'shaowcart.html',{'cart':cart})



class Plcaeorder_view(View):
    def get(self,request,*args,**kwargs):
        data=Orderform()
        return render(request,'order.html',{'d1':data})
    def post(self,request,*args,**kwargs):
        cart1=kwargs.get('cart')
        # cart2=kwargs.get('pro')
        user=request.user
        cart=Carts.objects.get(id=cart1)
        # s2=Product.objects.get(id=cart2)
        address=request.POST.get('address')
        Order.objects.create(user=user,address=address,cart=cart)
        cart.status='order-placed'
        cart.save()
        return redirect('home_view')
    
class DeleteCart(View):
    def get(self,request,*args,**kwargs):
        data=kwargs.get('id')
        d1=Carts.objects.get(id=data)
        d1.delete()
        return redirect('crtpr')