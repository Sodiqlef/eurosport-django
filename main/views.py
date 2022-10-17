from django.shortcuts import render
from .models import Match, D1Standing, D2Standing, CurrentSeason,Transfer, News

# Create your views here.

def home(request):
    matches = Match.objects.all().order_by('-date')
    d1 = D1Standing.objects.all().order_by('pos')
    return render(request, 'index.html', {'matches': matches, 'd1': d1})

def played_matches(request):
    matches = Match.objects.all().filter(played=True).order_by('-date')
    return render(request, 'all_matches.html', {'matches': matches})

def upcoming_matches(request):
    matches = Match.objects.all().filter(played=False).filter(live=False).order_by('-date')
    return render(request, 'all_matches.html', {'matches': matches})

def match_details(request, pk):
    match = Match.objects.get(pk=pk)
    home_standing = D1Standing.objects.all().filter(club=match.home).filter(season=match.season)
    away_standing = D1Standing.objects.all().filter(club=match.away).filter(season=match.season)
    prev = Match.objects.all().filter(home=match.home).filter(away=match.away).filter(played=True).order_by('-date')
    return render(request, 'details.html', {
        'match': match, 'prev': prev, 'home_standing': home_standing, 'away_standing': away_standing
    })


def standings(request):
    current_season = CurrentSeason.objects.all()
    for currents in current_season:
        current = currents.current_season
        d1 = D1Standing.objects.all().order_by('pos')
        d2 = D2Standing.objects.all().order_by('pos')
        return render(request, 'standings.html', {'d1': d1, 'd2': d2, 'current':current})


def transfer(request):
    all_transfer = Transfer.objects.all().order_by('-transferred_date')
    return render(request, 'transfer.html', {'all_transfer': all_transfer})


def news(request):
    all_news = News.objects.all().order_by('-date')
    return render(request, 'news.html', {'all_news': all_news})