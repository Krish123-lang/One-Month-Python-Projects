from django.shortcuts import render, redirect, get_object_or_404

from blog.forms import PostForm
from blog.models import Post
from django.contrib import messages

# Create your views here.


def index(request):
    posts = Post.objects.all()
    context = {
        "posts": posts
    }
    return render(request, "blog/index.html", context)


def create_post(request):
    if request.method == "GET":
        context = {"postform": PostForm()}
        return render(request, "blog/create_post.html", context)
    elif request.method == "POST":
        postform = PostForm(request.POST)
        if postform.is_valid():
            postform.save()
            messages.success(request, "The post has been created successfully!")
            return redirect('index')
        else:
            messages.error(request, "Something went wrong!")
            return render(request, "blog/create_post.html", {'postform': postform})


def edit_post(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == "GET":
        context = {"postform": PostForm(instance=post), "id": id}
        return render(request, "blog/create_post.html", context)
    elif request.method == "POST":
        postform = PostForm(request.POST, instance=post)
        if postform.is_valid():
            postform.save()
            messages.success(request, "The post has been updated successfully!")
            return redirect('index')
        else:
            messages.error(request, "Something went wrong!")
            return render(request, "blog/create_post.html", {'postform': postform})


def delete_post(request, id):
    post = get_object_or_404(Post, pk=id)
    context = {"post": post}

    if request.method == "GET":
        return render(request, "blog/post_confirm_delete.html", context)
    elif request.method == "POST":
        post.delete()
        messages.success(request, "Post deleted succcessfully!")
        return redirect('index')
