from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post
from django.views.generic import (
    ListView, 
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

# Create your views here.
def home(request):
    context = {
        'posts': Post.objects.all(),
        'title': 'Home',
    }
    return render(request, 'bandwagon/home.html/', context)

class PostListView(ListView):
    model = Post
    template_name = 'bandwagon/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 4

class UserPostListView(ListView):
    model = Post
    template_name = 'bandwagon/user_posts.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 4

    def get_queryset(self):
        user = get_object_or_404(User, username = self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')

class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content', 'image']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content', 'image']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post   
    success_url = '/'   

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False

def about(request):
    context = {
        'author': 'Brent Dolan',
        'title': 'About',
    }
    return render(request, 'bandwagon/about.html/', context)

def podcast(request):
    context = {
        'itunes': 'https://podcasts.apple.com/us/podcast/the-bandwagon-an-nba-podcast/id1434981308',
        'google_music': 'https://play.google.com/music/m/I5y2ybgdupaykko534kmueg4lme?t=The_Bandwagon_An_NBA_Podcast',
        'spotify': 'https://open.spotify.com/show/5LcSmChiRtgNo2gYY5qEpo',
        'tune_in': 'http://tun.in/pi7IL',
        'stitcher': 'https://www.stitcher.com/podcast/the-bandwagon-a-basketball-podcast',
        'title': 'Podcast',
    }
    return render(request, 'bandwagon/podcast.html/', context)


