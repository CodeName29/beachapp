from django.shortcuts import render

# Create your views here.
def log_in(request):
    return render(request, 'blog/log_in.html', {})

def sign_up(request):
    return render(request, 'blog/sign_up.html', {})


