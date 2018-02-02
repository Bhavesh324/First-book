from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post
# Create your views here.
def post_list(request):
	posts=Post.objects.all()#filter(published_date=timezone.now())#.ordered_by('published_date')
	return render(request, 'book/post_list.html', {'p': posts})
	
def pd(request,pk):
	post=get_object_or_404(Post,pk=pk)
	return render(request, 'book/pd.html', {'p':post})