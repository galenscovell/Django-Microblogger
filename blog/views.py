from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from .forms import PostForm, CommentForm


def main_page(request):
    page_title = 'µBlog'
    return render(request, 'blog/index.html', {"page_title": page_title})


def post_list(request):
    posts = Post.objects.order_by('-created_at')
    page_title = 'Post Grid'
    return render(request, 'blog/all.html', {"posts": posts, "page_title": page_title})


def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    page_title = post.title
    return render(request, 'blog/detail.html', {"post": post, "page_title": page_title})
    

def post_new(request):
    page_title = "New Post"
    if request.method == "POST":
        # ...then use POST request data from form
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('blog.views.post_detail', post_id=post.pk)
    else:
        # First time, display blank PostForm...
        form = PostForm()
    return render(request, 'blog/post_form.html', {"form": form, "page_title": page_title})

