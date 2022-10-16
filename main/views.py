from django.shortcuts import render
from .models import Match, D1Standing, D2Standing

# Create your views here.

def home(request):
    matches = Match.objects.all()
    d1 = D1Standing.objects.all()
    return render(request, 'index.html', {'matches': matches, 'd1': d1})

def match_details(request, pk):
    match = Match.objects.get(pk=pk)
    return render(request, 'details.html', {'match': match})
