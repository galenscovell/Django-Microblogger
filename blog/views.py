from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from .forms import PostForm, CommentForm, UserForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout


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


def user_login(request):
    page_title = "Login"
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return redirect('blog.views.main_page')
            else:
                message = "Inactive account credentials."
                return render(request, 'blog/login.html', {"page_title": page_title, "message": message})
        else:
            message = "No match found for those credentials."
            return render(request, 'blog/login.html', {"page_title": page_title, "message": message})
    else:
        return render(request, 'blog/login.html', {"page_title": page_title})


@login_required
def user_logout(request):
    page_title = "Login"
    logout(request)
    message = "User logged out."
    return render(request, 'blog/login.html', {"page_title": page_title, "message": message})


def user_register(request):
    page_title = "Registration"
    registered = False
    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True
        else:
            return render(request, 'blog/register.html', {"form": user_form, "registered": registered, "page_title": page_title})
    else:
        user_form = UserForm()
    return render(request, 'blog/register.html', {"form": user_form, "registered": registered, "page_title": page_title})


@login_required
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

