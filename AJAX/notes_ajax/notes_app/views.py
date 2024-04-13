from django.shortcuts import render, redirect
from django.views.generic import View
from .models import Post
# Create your views here.

class Posts(View):
  template = 'index.html'
  context = {}
  def get(self, request):
    self.context['posts'] = Post.objects.all()
    return render(request, self.template, self.context)
  
  def post(self, request):
    Post.objects.create(post=request.POST['post'])
    return redirect('/')