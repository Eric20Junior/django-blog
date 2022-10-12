from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Post, Comment
from .forms import CommentForm, PostForm, NewUserForm

# Create your views here.
def loginView(request):
    page = 'login'

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User doest not exit')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'You have successfully logged in.')
            return redirect('home')
        else:
            messages.error(request, 'Username or Password does not exit')

    return render(request, 'feed/login_register.html', {'page': page})

def logoutView(request):
    logout(request)
    messages.success(request, 'You have successfully logged out.')
    return redirect('home')

def registerPage(request):
    form = NewUserForm()

    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            messages.success(request, 'Registration Successful')
            return redirect('home')
        else:
            messages.error(request, 'An error ocurred during registration')
    return render(request, 'feed/login_register.html', {'form': form})

def home(request):
    posts = Post.objects.all()

    context = {'posts':posts}
    return render(request, 'feed/home.html', context)

def createView(request):
    form = PostForm()

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('home')

    else:
        form = PostForm()

    return render(request, 'feed/create-post.html', {'form':form})

def detailsView(request, pk):
    posts = Post.objects.get(id=pk)
    comments = posts.comment_set.all()

    if request.method == 'POST':
        message = Comment.objects.create(
            user=request.user,
            post=posts,
            body=request.POST.get('body')
        )
    return render(request, 'feed/details_page.html', {'posts': posts, 'comments':comments})

def updateView(request, pk):
    posts = Post.objects.get(id=pk)
    form = PostForm(instance=posts)

    if request.user != posts.author:
        return HttpResponse('Oops!!! You are not allowed here!!!')

    if request.method == 'POST':
        form = PostForm(request.POST, instance=posts)
        if form.is_valid():
            form.save()
        return redirect('home')
    context = {'form':form, 'posts':posts}
    return render(request, 'feed/update-post.html', context)

def deleteView(request, pk):
    posts = Post.objects.get(id=pk)

    if request.user != posts.author:
        return HttpResponse('Oops!!! You are not allowed here!!!')

    if request.method == 'POST':
        posts.delete()
        return redirect('home')
    return render(request, 'feed/delete.html', {'obj':posts})

def deleteMessage(request, pk):
    comment = Comment.objects.get(id=pk)

    if request.user != comment.user:
        return HttpResponse('Oops!!! You are not allowed here!!!')

    if request.method == 'POST':
        comment.delete()
        messages.success(request, 'You have successfully deleted your comment.')
        return redirect('home')
    return render(request, 'feed/delete.html', {'obj':comment})