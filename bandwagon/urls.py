from django.urls import path
from . import views
from .views import (
    PostListView, 
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView
)

urlpatterns = [
    path('', PostListView.as_view(), name="bandwagon-home"),
    path('about/', views.about, name='bandwagon-about'),
    path('playfinder/', views.playfinder, name='playfinder'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('post/new/', PostCreateView.as_view(), name = 'post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('podcast/', views.podcast, name='bandwagon-podcast'),
    path('scores/', views.scores, name='bandwagon-scores'),
    path('teams/', views.teams, name='bandwagon-teams'),
    path('team/<str:city>/<str:name>/<str:logo_url>/<str:abbr>/', views.TeamDetailView, name='bandwagon-team'),
    path('player/<str:player_initial>/<str:player_id>/', views.PlayerDetailView, name='bandwagon-player'),
]