from django.shortcuts import render

from .models import Post, Group

def index(request):
    latest = Post.objects.order_by("-pub_date")
    return render(request, "index.html", {"posts": latest})
