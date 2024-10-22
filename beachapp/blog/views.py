from django.shortcuts import render
from django.utils import timezone
from .models import Post
# Create your views here.
def log_in(request):
    posts=Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/log_in.html', {'posts': posts})

def sign_up(request):
    return render(request, 'blog/sign_up.html', {})




