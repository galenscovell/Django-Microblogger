from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment


def main_page(request):
    page_title = 'Index'
    return render(request, 'blog/index.html', {"page_title": page_title})


def post_list(request):
    posts = Post.objects.order_by('created_at')
    page_title = 'All'
    return render(request, 'blog/all.html', {"page_title": page_title, "posts": posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/detail.html', {"post": post})
    

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('blog.views.post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_new.html', {"form": form})

# def topic_cloud