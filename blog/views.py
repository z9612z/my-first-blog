from django.shortcuts import render
from django.utils import timezone
from .models import Post # 현재 디렉토리의 models.py를 가져온다는 의미 .py 생략

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts' : posts})
