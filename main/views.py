from django.shortcuts import get_object_or_404, render
from .models import Match, D1Standing, D2Standing, CurrentSeason,Transfer, News
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

played = 'PLAYED'
upcoming = 'UPCOMING'

def paging(val, queryset, request):
    page = request.GET.get('page', 1)
    paginator = Paginator(queryset, val)
    try:
        matches = paginator.page(page)
    except PageNotAnInteger:

        matches = paginator.page(1)
    except EmptyPage:
        matches = paginator.page(paginator.num_pages)

    return matches


def home(request):
    queryset_result = Match.objects.all().filter(played=True).order_by('-date')
    queryset_fixtures = Match.objects.all().filter(played=False).order_by('-date')
    queryset_live = Match.objects.all().filter(live=True).order_by('-date')
    d1 = D1Standing.objects.all().order_by('pos')
    results = paging(4, queryset_result, request)
    fixtures = paging(4, queryset_fixtures, request)
    live = paging(4, queryset_live, request)
    return render(request, 'index.html', {'results': results, 'fixtures': fixtures, 'd1': d1, 'live': live})

def played_cl(request):
    queryset = Match.objects.all().filter(played=True).filter(competition='Champions League').order_by('-date')
    matches = paging(20, queryset, request)
    return render(request, 'all_matches.html', {'matches': matches, 'played': played, 'queryset':queryset})

def upcoming_cl(request):
    queryset = Match.objects.all().filter(played=False).filter(live=False).filter(competition='Champions League').order_by('-date')
    matches = paging(20, queryset, request)
    return render(request, 'all_matches.html', {'matches': matches, 'upcoming': upcoming})

def played_el(request):
    queryset = Match.objects.all().filter(played=True).filter(competition='Europa League').order_by('-date')
    matches = paging(20, queryset, request)
    return render(request, 'all_matches.html', {'matches': matches, 'played': played})

def upcoming_el(request):
    queryset = Match.objects.all().filter(played=False).filter(live=False).filter(competition='Europa League').order_by('-date')
    matches = paging(20, queryset, request)
    return render(request, 'all_matches.html', {'matches': matches, 'upcoming': upcoming})

def played_d1(request):
    queryset = Match.objects.all().filter(played=True).filter(competition='Division 1 League').order_by('-date')
    matches = paging(20, queryset, request)
    return render(request, 'all_matches.html', {'matches': matches, 'played': played})

def upcoming_d1(request):
    queryset = Match.objects.all().filter(played=False).filter(live=False).filter(competition='Division 1 League').order_by('-date')
    matches = paging(20, queryset, request)
    return render(request, 'all_matches.html', {'matches': matches, 'upcoming': upcoming})

def played_d2(request):
    queryset = Match.objects.all().filter(played=True).filter(competition='Division 2 League').order_by('-date')
    matches = paging(20, queryset, request)
    return render(request, 'all_matches.html', {'matches': matches, 'played': played})

def upcoming_d2(request):
    queryset = Match.objects.all().filter(played=False).filter(live=False).filter(competition='Division 2 League').order_by('-date')
    matches = paging(20, queryset, request)
    return render(request, 'all_matches.html', {'matches': matches, 'upcoming': upcoming})

def played_d2_cup(request):
    queryset = Match.objects.all().filter(played=True).filter(competition='League Cup, Division 2').order_by('-date')
    matches = paging(20, queryset, request)
    return render(request, 'all_matches.html', {'matches': matches, 'played': played})

def upcoming_d2_cup(request):
    queryset = Match.objects.all().filter(played=False).filter(live=False).filter(competition='League Cup, Division 2').order_by('-date')
    matches = paging(20, queryset, request)
    return render(request, 'all_matches.html', {'matches': matches, 'upcoming': upcoming})

def played_d1_cup(request):
    queryset = Match.objects.all().filter(played=True).filter(competition='League Cup, Division 1').order_by('-date')
    matches = paging(20, queryset, request)
    return render(request, 'all_matches.html', {'matches': matches, 'played': played})

def upcoming_d1_cup(request):
    queryset = Match.objects.all().filter(played=False).filter(live=False).filter(competition='League Cup, Division 1').order_by('-date')
    matches = paging(20, queryset, request)
    return render(request, 'all_matches.html', {'matches': matches, 'upcoming': upcoming})

def played_super_cup(request):
    queryset = Match.objects.all().filter(played=True).filter(competition='Super Cup').order_by('-date')
    matches = paging(20, queryset, request)
    return render(request, 'all_matches.html', {'matches': matches, 'played': played})

def upcoming_super_cup(request):
    queryset = Match.objects.all().filter(played=False).filter(live=False).filter(competition='Super Cup').order_by('-date')
    matches = paging(20, queryset, request)
    return render(request, 'all_matches.html', {'matches': matches, 'upcoming': upcoming})

def played_international(request):
    queryset = Match.objects.all().filter(played=True).filter(competition='International Match').order_by('-date')
    matches = paging(20, queryset, request)
    return render(request, 'all_matches.html', {'matches': matches, 'played': played})

def upcoming_international(request):
    queryset = Match.objects.all().filter(played=False).filter(live=False).filter(competition='International Match').order_by('-date')
    matches = paging(20, queryset, request)
    return render(request, 'all_matches.html', {'matches': matches, 'upcoming': upcoming})

def match_details(request, pk):
    match = get_object_or_404(Match, pk=pk)
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

def prev_standings(request):
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
    queryset = News.objects.all().order_by('-date')
    matches = paging(15, queryset, request)
    return render(request, 'news.html', {'matches': matches})


def news_details(request, pk):
    news = get_object_or_404(News, pk=pk)
    return render(request, 'news_details.html', {'news': news})