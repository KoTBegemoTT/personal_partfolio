from django.shortcuts import render
from .models import Blog
from django.shortcuts import get_object_or_404


app_name = 'blog'


def all_blogs(request):
    blogs = Blog.objects.all()
    return render(request, r'blog\all_blogs.html', {'blogs': blogs, 'posts_count': len(blogs)})


def post(request, post_title):
    post = get_object_or_404(Blog, title=post_title)
    print(post.title)
    return render(request, r'blog\post.html', {'post': post})
