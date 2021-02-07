from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from datetime import datetime
from .models import Post

# Create your views here.


def homepage(request):
    posts = Post.objects.all()
    now = datetime.now()
    return render(request, 'index.html', locals())
    # post_list = list()
    # for count, post in enumerate(posts):
    #    post_list.append("No.{}:".format(str(count)) + str(post)+"<hr>")
    #    post_list.append("<small>" + str(post.body) + "</small><br><br>")
    # return HttpResponse(post_list)


def showpost(request, slug):
    try:
        post = Post.objects.get(slug=slug)
        if post != None:
            return render(request, 'post.html', locals())
    except:
        return redirect('/')