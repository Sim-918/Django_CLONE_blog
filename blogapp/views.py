from django.shortcuts import render
from blogapp.models import Category,Post
from django.views import generic

# Create your views here.
def index(request):
    post_latest=Post.objects.order_by("-createDate")[:4]      #블로그를 최신순으로 (내림차순)
    context={
        "post_latest":post_latest
    }
    return render(request,"index.html",context=context)

class PostDetailViews(generic.DetailView):
    model=Post
