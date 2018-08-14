from django.shortcuts import render
from django.utils import timezone 
from tracker.models import Post
                                                                                                                                            
def tracker_data(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'tracker/tracker_data.html', {'posts': posts})
