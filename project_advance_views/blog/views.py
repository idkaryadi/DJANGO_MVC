from django.shortcuts import render, redirect
from .models import Blog
from .forms import BlogForm

# Create your views here.
def blog(request):
    blog = Blog.objects.all()
    return render(request, 'blog/blog.html', {'blogs':blog})

def post_detail(request, post_id):
    blog = Blog.objects.get(pk = post_id)
    return render(request, 'blog/post_detail.html', {'blog':blog})

def input_post(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(blog) #
    
    else:
        form = BlogForm()
    return render(request, 'blog/post_new.html', {'form':form})