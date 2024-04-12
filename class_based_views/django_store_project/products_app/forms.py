from django import forms
from .models import Product
from .validations import *


class ProductForm(forms.ModelForm):
  class Meta:
    model = Product
    fields = ['manufacturer', 'name', 'price', 'description']
    widgets={
      "description": forms.Textarea(attrs={'rows':3, 'cols': 5}),
    }

  def clean_name(self):
    data = self.cleaned_data['name']
    validate_product_name_length(data)
    return data
  
  def clean_price(self):
    data = self.cleaned_data['price']
    validate_product_price(data)
    return data
  
  def clean_description(self):
    data = self. cleaned_data['description']
    validate_product_description(data)
    return data