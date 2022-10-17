from django.contrib import admin
from main.models import Match, D1Standing, D2Standing,CurrentSeason, News, Transfer

# Register your models here.
admin.site.register(Match)
admin.site.register(D1Standing)
admin.site.register(D2Standing)
admin.site.register(CurrentSeason)
admin.site.register(News)
admin.site.register(Transfer)



