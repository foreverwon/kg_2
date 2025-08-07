from django.shortcuts import render
from poster.models import Poster
#from freeboard.models import Post
from datetime import datetime, timedelta

# Create your views here.

def main_page(request):
    today = datetime.today().date()
    highlight = Poster.objects.order_by('-prize').first()
    new_posters = Poster.objects.order_by('-created_at')[:6]
    hot_posters = Poster.objects.order_by('-views')[:6]
    closing_soon = Poster.objects.filter(end_date__range=[today, today + timedelta(days=3)])

    context = {
        'highlight': highlight,
        'new_posters': new_posters,
        'hot_posters': hot_posters,
        'closing_soon': closing_soon,
    }
    return render(request, 'home/main.html', context)

from django.shortcuts import render

def main_page(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def ongoing(request):
    return render(request, 'poster/ongoing.html')  # 필요시 context 추가

def closed(request):
    return render(request, 'poster/closed.html')

def detail(request):
    return render(request, 'poster/detail.html')  # 필요시 context 추가

# 마이페이지
def mypage_profile(request):
    return render(request, 'mypage/profile.html')

def mypage_saved(request):
    return render(request, 'mypage/saved.html')

def mypage_myposts(request):
    return render(request, 'mypage/myposts.html')

def mypage_mycomments(request):
    return render(request, 'mypage/mycomments.html')
