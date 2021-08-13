
from django.shortcuts import render
from django.http import HttpResponse

from.models import Blogpost


# Create your views here.

def index(request):
    mypost=Blogpost.objects.all()
    print(mypost)
    return render(request, 'blog/index.html')

def blogpost(request):

    return render(request, 'blog/blogpost.html')
