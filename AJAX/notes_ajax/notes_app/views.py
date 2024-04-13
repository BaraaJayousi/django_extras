from django.shortcuts import render, redirect
from django.views.generic import View
from .models import Post
# Create your views here.


class Index(View):
  template = 'index.html'
  context = {}
  def get(self, request):
    self.context['posts'] = Post.objects.all()
    return render(request, self.template, self.context)
  
class Posts(View):
  template = 'posts_template.html'
  context = {}
  def get(self, request):
    self.context['posts'] = Post.objects.all()
    return render(request, self.template, self.context)
  
  def post(self, request):
    if request.POST['action'] == 'post':
      Post.objects.create(post=request.POST['post'])
    elif request.POST['action'] == 'delete':
      post = Post.objects.filter(id = request.POST['post_id']).first()
      if post:
        post.delete()
        print('deleted post successfully ')

    # print('updating posts list')
    # self.context['posts'] = Post.objects.all()
    return redirect('/posts')