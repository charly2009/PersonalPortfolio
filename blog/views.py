from django.shortcuts import render, get_object_or_404
from .models import Blog # grab the model created in models and put it in dictionary then display it in web

# Create your views here.
def allblog(request):
    blogs= Blog.objects
    return render(request, 'blog/blogs.html', {'blogs': blogs})

def detail(request, blog_id ):
    blogdetail = get_object_or_404(Blog, pk= blog_id) # pk = primary key
    return render(request, 'blog/detail.html', {'blog': blogdetail})