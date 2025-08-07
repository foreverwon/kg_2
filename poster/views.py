# poster/views.py

from django.shortcuts import render, get_object_or_404
from .models import Poster
from django.db.models import Q
from datetime import date

def home(request):
    query = request.GET.get('q', '')
    selected_category = request.GET.get('category', '')

    posters = Poster.objects.all()

    if query:
        posters = posters.filter(
            Q(title__icontains=query) |
            Q(organization__icontains=query) |
            Q(description__icontains=query)
        )

    if selected_category:
        posters = posters.filter(category=selected_category)

    # 중복 없는 카테고리 목록 추출
    categories = Poster.objects.values_list('category', flat=True).distinct()

    return render(request, 'home/main.html', {
        'posters': posters.order_by('-id'),
        'query': query,
        'selected_category': selected_category,
        'categories': categories
    })

def poster_list(request):
    query = request.GET.get('q', '')  #검색어
    selected_category = request.GET.get('category', '')   #카테고리 필터

    posters = Poster.objects.all()
    # 검색 필터
    if query:
        posters = posters.filter(
            Q(title__icontains=query) |
            Q(organization__icontains=query) |
            Q(description__icontains=query)
        )

    # 카테고리 필터
    if selected_category:
        posters = posters.filter(category=selected_category)

    # 중복 없는 카테고리 목록
    categories = Poster.objects.values_list('category', flat=True).distinct()

    return render(request, 'home/main.html', {
    'posters': posters.order_by('-id'),
    'query': query,
    'selected_category': selected_category,
    'categories': categories
})

def poster_detail(request, pk):
    poster = get_object_or_404(Poster, pk=pk)
    poster.views += 1  # 조회수 1 증가
    poster.save()      # DB에 저장
    return render(request, 'poster/poster_detail.html', {'poster': poster})

def ongoing_contests(request):
    today = date.today()
    contests = Poster.objects.filter(end_date__gte=today).order_by('end_date')
    return render(request, 'poster/ongoing.html', {'contests': contests})

def closed_contests(request):
    today = date.today()
    contests = Poster.objects.filter(end_date__lt=today).order_by('-end_date')
    return render(request, 'poster/closed.html', {'contests': contests})