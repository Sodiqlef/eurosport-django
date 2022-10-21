from django.contrib import admin
from main.models import Match, D1Standing, D2Standing,Currentedition, News, Transfer, Club, Player

# Register your models here.

def search(val):
    class SearchAdmin(admin.ModelAdmin):
        search_fields =val
    return SearchAdmin



admin.site.register(Match, search(['home', 'away']))
admin.site.register(D1Standing, search(['club']))
admin.site.register(D2Standing, search(['club']))
admin.site.register(Currentedition)
admin.site.register(News, search(['subject']))
admin.site.register(Transfer, search(['player_name']))
admin.site.register(Club, search(['name']))
admin.site.register(Player, search(['name']))



