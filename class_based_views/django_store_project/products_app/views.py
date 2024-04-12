from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import *
from .models import Product

# Create your views here.

def index(request):
  return redirect('/products')

class Products(View):
  render_template = "products.html"
  product_form = ProductForm()
  context = {
    "product_form": product_form,
    "products": []
  }
  def get(self, request):
    self.context['products'] = Product.objects.all()
    return render(request, self.render_template, self.context)
  
  def post(self, request):
    bound_product= ProductForm(request.POST)
    if bound_product.is_valid():
      bound_product.save()
      return redirect('/')
    return render(request,  self.render_template, {"product_form": bound_product} )
  
class EditProduct(View):
  render_template = 'product_details.html'
  context={  }
  def get(self,request, id):
    if self.check_valid_product(id):
      return render(request, self.render_template, self.context)
    return redirect('/')

  def post(self, request, id):
    print("getting post request")
    if request.POST['action'] == "Update":
      if self.check_valid_product(id):
        bound_product= ProductForm(request.POST, instance= self.context['product'])
        if bound_product.is_valid():
          bound_product.save()
          return redirect('/')
        # if invalid inputs resend the form with error messages
        self.context['product_form'] = bound_product
    elif request.POST['action'] == "Delete":
      if self.check_valid_product(id):
        Product.objects.delete_product(id)
      return redirect('/')

    return render(request, self.render_template, self.context)
  

  def check_valid_product(self,id):
    product = Product.objects.get_product(id = id)
    if product:
      product_form = ProductForm(instance=product)
      self.context['product_form'] = product_form
      self.context['product'] = product
      return True