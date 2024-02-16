from django import forms
from django.contrib.auth.models import User
from ecom.models import Carts,Order




class Useregister(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','email','password'] 
        widgets={
            'first_name':forms.Textarea(attrs={'class':'form-control','placeholder':'first_name'}),
            'last_name':forms.Textarea(attrs={'class':'form-control','placeholder':'last_name'}),
            'username':forms.Textarea(attrs={'class':'form-control','placeholder':'username'}),
            'password':forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}),
            'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'email'}),
 }
class LoginForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','password']
        widgets={
             'username':forms.Textarea(attrs={'class':'form-control','placeholder':'username'}),
            'password':forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}),}

class cartForm(forms.ModelForm):
    class Meta:
        model=Carts
        fields=['quantity']
        widgets={
        'quantity':forms.NumberInput(attrs={'class':'form-control'})
        
        }

class Orderform(forms.ModelForm):
    class Meta:
        model=Order
        fields=['address']
        widgets={
        'address':forms.TextInput(attrs={'class':'form-control'})
        
        }