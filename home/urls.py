from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.main_page, name='index'),  # 기존 유지
    path('about/', views.about, name='about'),
    path('poster/ongoing/', views.ongoing, name='ongoing'),
    path('poster/closed/', views.closed, name='closed'),
    path('poster/detail/', views.detail, name='detail'),

    # 마이페이지
    path('mypage/profile/', views.mypage_profile, name='mypage_profile'),
    path('mypage/saved/', views.mypage_saved, name='mypage_saved'),
    path('mypage/myposts/', views.mypage_myposts, name='mypage_myposts'),
    path('mypage/mycomments/', views.mypage_mycomments, name='mypage_mycomments'),
]