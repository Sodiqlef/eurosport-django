from django.shortcuts import get_object_or_404, render
from .models import Match, D1Standing, D2Standing, Currentedition,Transfer, News, Club, Player
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from  django.db.models import Q

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
    d1 = D1Standing.objects.all().order_by('-pts')
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
    home_standing = D1Standing.objects.all().filter(club=match.home).filter(edition=match.edition)
    away_standing = D1Standing.objects.all().filter(club=match.away).filter(edition=match.edition)
    prev = Match.objects.all().filter(home=match.home).filter(away=match.away).filter(played=True).order_by('-date')
    return render(request, 'details.html', {
        'match': match, 'prev': prev, 'home_standing': home_standing, 'away_standing': away_standing
    })


def standings(request):
    current_edition = Currentedition.objects.all()
    prev_edition = Currentedition.objects.last()
    prev = range(prev_edition.current_edition)
    search = request.GET.get('prevStandings')
    search2 = request.GET.get('prevStandings2')
    for currents in current_edition:
        current = currents.current_edition
        smth = current-1
        if search2:
            d1 = D1Standing.objects.filter(Q(edition__icontains=search)).order_by('-pts')
            d2 = D2Standing.objects.filter(Q(edition__icontains=search2)).order_by('-pts')
        else:
            d1 = D1Standing.objects.all().order_by('-pts')
            d2 = D2Standing.objects.all().order_by('-pts')
        return render(request, 'standings.html', {'d1': d1, 'd2': d2, 'current':current, 'prev': prev, 'smth': smth})

def d1_prev_standings(request):
    current_edition = Currentedition.objects.all()
    prev_edition = Currentedition.objects.last()
    prev = range(prev_edition.current_edition)
    search = request.GET.get('prevStandings')
    div = 1
    if search:
        d = D1Standing.objects.filter(Q(edition__icontains=search)).order_by('-pts')
    else:
        d = D1Standing.objects.all().order_by('-pts')
    for currents in current_edition:
        current = currents.current_edition
        smth = current-1
        return render(request, 'prev_standings.html', {'d': d, 'div':div, 'prev': prev, 'smth': smth, 'search':search})

def d2_prev_standings(request):
    current_edition = Currentedition.objects.all()
    prev_edition = Currentedition.objects.last()
    prev = range(prev_edition.current_edition)
    search2 = request.GET.get('prevStandings2')
    div = 2
    if search2:
        d = D1Standing.objects.filter(Q(edition__icontains=search2)).order_by('-pts')
    else:
        d = D2Standing.objects.all().order_by('-pts')
    for currents in current_edition:
        current = currents.current_edition
        smth = current-1
        return render(request, 'prev_standings.html', {'d': d, 'div':div, 'prev': prev, 'smth': smth, 'search2':search2})



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


def club(request):
    clubs = Club.objects.all().order_by('-division')
    return render(request, 'club_details.html', {'clubs': clubs})

def club_details(request, pk):
    clubs = get_object_or_404(Club, pk=pk)
    return render(request, 'club_details.html', {'clubs': clubs})


def player(request):
    search = request.GET.get('players')
    if search:
        queryset = Player.objects.filter(Q(name__icontains=search)).order_by('-name')
        players = paging(20, queryset, request)
    else:
        queryset = Player.objects.all().order_by('-name')
        players = paging(20, queryset, request)

    return render(request, 'players.html', {'players': players, 'matches': players})