from django.urls import path
from . import views
from django.views.generic import TemplateView


app_name = 'poster'

urlpatterns = [
    path('', views.poster_list, name='poster_list'), #전체 공모전
    path('<int:pk>/', views.poster_detail, name='poster_detail'),  # ✅ 상세 보기
    path('ongoing/', views.ongoing_contests, name='ongoing'),  # 진행중인 공모전
    path('closed/', views.closed_contests, name='closed'),     # 마감된 공모전
]