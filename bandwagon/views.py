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

def scores(request):
    context = {
        'kings_score': '98',
        'lakers_score': '106',
        'title': 'Scores',
    }
    return render(request, 'bandwagon/scores.html/', context)

def teams(request):
    context = {
        'teams': {
            'hawks': {
                'city': 'Atlanta',
                'name': 'Hawks',
                'logo': 'atlanta-logo.png',
                'color': '',
            },
            'celtics': {
                'city': 'Boston',
                'name': 'Celtics',
                'logo': 'boston-logo.png',
                'color': '',
            },
            'nets': {
                'city': 'Brooklyn',
                'name': 'Nets',
                'logo': 'brooklyn-logo.png',
                'color': '',
            },
            'hornets': {
                'city': 'Charlotte',
                'name': 'Hornets',
                'logo': 'charlotte-logo.png',
                'color': '',
            },
            'bulls': {
                'city': 'Chicago',
                'name': 'Bulls',
                'logo': 'chicago-logo.jpg',
                'color': '',
            },
            'cavs': {
                'city': 'Cleveland',
                'name': 'Cavaliers',
                'logo': 'cleveland-logo.jpg',
                'color': '',
            },
            'mavs': {
                'city': 'Dallas',
                'name': 'Mavericks',
                'logo': 'dallas-logo.jpg',
                'color': '',
            },
            'nuggets': {
                'city': 'Denver',
                'name': 'Nuggets',
                'logo': 'denver-logo.png',
                'color': '',
            },
            'pistons': {
                'city': 'Detroit',
                'name': 'Pistons',
                'logo': 'detroit-logo.png',
                'color': '',
            },
            'warriors': {
                'city': 'Golden State',
                'name': 'Warriors',
                'logo': 'golden-state-logo.jpg',
                'color': '',
            },
            'rockets': {
                'city': 'Houston',
                'name': 'Rockets',
                'logo': 'houston-logo.png',
                'color': '',
            },
            'pacers': {
                'city': 'Indiana',
                'name': 'Pacers',
                'logo': 'indiana-logo.png',
                'color': '',
            },
            'clippers': {
                'city': 'Los Angeles',
                'name': 'Clippers',
                'logo': 'la-clippers-logo.png',
                'color': '',
            },
            'lakers': {
                'city': 'Los Angeles',
                'name': 'Lakers',
                'logo': 'la-lakers-logo.png',
                'color': '',
            },
            'grizzlies': {
                'city': 'Memphis',
                'name': 'Grizzlies',
                'logo': 'memphis-logo.png',
                'color': '',
            },
            'heat': {
                'city': 'Miami',
                'name': 'Heat',
                'logo': 'miami-logo.png',
                'color': '',
            },
            'bucks': {
                'city': 'Milwaukee',
                'name': 'Bucks',
                'logo': 'milwaukee-logo.jpg',
                'color': '',
            },
            'wolves': {
                'city': 'Minnesota',
                'name': 'Timberwolves',
                'logo': 'minnesota-logo.png',
                'color': '',
            },
            'pelicans': {
                'city': 'New Orleans',
                'name': 'Pelicans',
                'logo': 'new-orleans-logo.png',
                'color': '',
            },
            'knicks': {
                'city': 'New York',
                'name': 'Knicks',
                'logo': 'new-york-knicks-logo.png',
                'color': '',
            },
            'thunder': {
                'city': 'Oklahoma City',
                'name': 'Thunder',
                'logo': 'okc-logo.png',
                'color': '',
            },
            'magic': {
                'city': 'Orlando',
                'name': 'Magic',
                'logo': 'orlando-logo.png',
                'color': '',
            },
            'sixers': {
                'city': 'Philadelphia',
                'name': '76ers',
                'logo': 'philadelphia-logo.png',
                'color': '',
            },
            'suns': {
                'city': 'Phoenix',
                'name': 'Suns',
                'logo': 'phoenix-logo.png',
                'color': '',
            },
            'blazers': {
                'city': 'Portland',
                'name': 'Trailblazers',
                'logo': 'portland-logo.png',
                'color': '',
            },
            'kings': {
                'city': 'Sacramento',
                'name': 'Kings',
                'logo': 'sacramento-logo.jpg',
                'color': '',
            },
            'spurs': {
                'city': 'San Antonio',
                'name': 'Spurs',
                'logo': 'san-antonio-logo.jpg',
                'color': '',
            },
            'raptors': {
                'city': 'Toronto',
                'name': 'Raptors',
                'logo': 'toronto-logo.png',
                'color': '',
            },
            'jazz': {
                'city': 'Utah',
                'name': 'Jazz',
                'logo': 'utah-logo.png',
                'color': '',
            },
            'wizards': {
                'city': 'Washington',
                'name': 'Wizards',
                'logo': 'washington-logo.png',
                'color': '',
            },
        },
    }
    return render(request, 'bandwagon/teams.html/', context)

def TeamDetailView(request, city, name, logo_url): 
    context = {
        'city': city,
        'name': name,
        'logo': logo_url
    }
    return render(request, 'bandwagon/team.html/', context)