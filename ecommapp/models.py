from django.db import models

# Create your models here.

from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name

class Product(models.Model):
    p_id=models.CharField(max_length=15, primary_key=True)
    p_name = models.CharField(max_length=150)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,related_name="categories")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    description = models.TextField()
    image=models.ImageField(upload_to='product/')

    def __str__(self):
        return self.p_name

class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.product.name}"

from django.contrib.auth.models import User
from django.db import models

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)  # Add this field
    items = models.ManyToManyField('CartItem')

    def get_total_price(self):
        return sum(item.product.price * item.quantity for item in self.items.all())
