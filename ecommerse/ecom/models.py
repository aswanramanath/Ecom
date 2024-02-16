from django.db import models
from django.contrib.auth.models import User
class Category(models.Model):
    Category_name=models.CharField(max_length=100)
    is_active=models.BooleanField(default=True)
    def __str__(self):
        return self.Category_name 
class Product(models.Model):
    product_name=models.CharField(max_length=100)
    price=models.PositiveIntegerField()
    Category_name=models.ForeignKey(Category,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='img',null=True)
    discription=models.CharField(max_length=100)
    def __str__(self):
        return self.product_name

class Carts(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)
    options=(
('in-cart','in-cart'),
('cancelled','cancelled'),
('order-placed','order-placed'),

    )
    status=models.CharField(max_length=100,choices=options,default='in-cart')


class Order(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    cart=models.ForeignKey(Carts,on_delete=models.CASCADE)
    order_date=models.DateTimeField(auto_now_add=True)
    address=models.TextField(max_length=100)
    options=(
        ('order-placed','order-placed'),
        ('cancelled','cancelled'),
        ('delivered','delivered'),
        
        ('dispached','dispached'), 
        )
    status=models.CharField(max_length=100,choices=options,default='order-placed')
     
