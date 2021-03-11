from django.shortcuts import render, get_object_or_404
from .models import Post

def post_list(request):
    posts = Post.published.all()
    return render(request,'blog/post/list.html', {'post':post})

# Create your views here.
