from django import forms
from .models import Product, Category

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name','description']

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['p_id','p_name','category','price','stock','description','image']

