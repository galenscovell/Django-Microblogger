from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from .forms import PostForm, CommentForm, UserForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def about_page(request):
    page_title = 'About'
    return render(request, 'blog/about.html', {"page_title": page_title})


def post_list(request):
    posts = Post.objects.order_by('-created_at')
    page_title = 'Post Grid'
    return render(request, 'blog/all.html', {"posts": posts, "page_title": page_title})


def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    comments = Comment.objects.filter(post=post_id)
    page_title = post.title
    return render(request, 'blog/detail.html', {"post": post, "page_title": page_title, "comments": comments})


def user_login(request):
    page_title = "Login"
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return redirect('blog.views.post_list')
            else:
                messages.warning(request, 'Inactive account.')
        elif username == "" or password == "":
            messages.warning(request, 'All fields required.')
        else:
            messages.error(request, 'No match found.')
    return render(request, 'blog/login.html', {"page_title": page_title})


@login_required
def user_logout(request):
    page_title = "Login"
    logout(request)
    messages.success(request, 'User logged out.')
    return render(request, 'blog/login.html', {"page_title": page_title})


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
            messages.success(request, 'Registration complete.')
        else:
            messages.error(request, 'Registration error.')
    else:
        user_form = UserForm()
    return render(request, 'blog/register.html', {"form": user_form, "registered": registered, "page_title": page_title})


@login_required
def post_new(request):
    page_title = "New Post"
    if request.method == "POST":
        # ...then use POST request data from form
        post_form = PostForm(request.POST)
        if post_form.is_valid():
            post = post_form.save(commit=False)
            post.author = request.user
            if 'image' in request.FILES:
                post.image = request.FILES['image']
            post.save()
            messages.success(request, 'Post created.')
            return redirect('blog.views.post_detail', post_id=post.pk)
        else:
            messages.error(request, 'Posting error.')
    else:
        # First time, display blank PostForm...
        post_form = PostForm()
    return render(request, 'blog/post_form.html', {"form": post_form, "page_title": page_title})


@login_required
def post_edit(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    page_title = "Editing: " + post.title
    if request.method == "POST":
        post_form = PostForm(request.POST, instance=post)
        if post_form.is_valid():
            post = post_form.save(commit=False)
            post.author = request.user
            if 'image' in request.FILES:
                post.image = request.FILES['image']
            post.update()
            messages.success(request, 'Post edited.')
            return redirect('blog.views.post_detail', post_id=post.pk)
        else:
            messages.error(request, 'Editing error.')
    else:
        post_form = PostForm(instance=post)
    return render(request, 'blog/post_form.html', {'form': post_form, "page_title": page_title})

@login_required
def post_delete(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.delete()
    messages.success(request, 'Post deleted.')
    return redirect('blog.views.post_list')

@login_required
def post_like(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.favorites += 1
    post.save()
    messages.success(request, 'Post favorited.')
    return redirect('blog.views.post_detail', post_id=post.pk)

@login_required
def comment_add(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    comment = Comment()
    comment.author = request.user
    comment.post = post
    comment.content = request.POST['content']
    comment.save()
    return redirect('blog.views.post_detail', post_id=post.pk)

@login_required
def comment_upvote(request, post_id, comment_id):
    post = get_object_or_404(Post, pk=post_id)
    comment = get_object_or_404(Comment, pk=comment_id)
    comment.votes += 1
    comment.save()
    return redirect('blog.views.post_detail', post_id=post.pk)

@login_required
def comment_downvote(request, post_id, comment_id):
    post = get_object_or_404(Post, pk=post_id)
    comment = get_object_or_404(Comment, pk=comment_id)
    comment.votes -= 1
    comment.save()
    return redirect('blog.views.post_detail', post_id=post.pk)