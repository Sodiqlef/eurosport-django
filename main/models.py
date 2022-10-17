from django.db import models

# Create your models here.

match_status = (
    ("Division 1 League", "Division 1 League"),
    ("Division 2 League ", "Division 2 League"),
    ("League Cup, Division 1", "League Cup, Division 1"),
    ("League Cup, Division 2", "League Cup, Division 2"),
    ("Champions League", "Champions League"),
    ("Europa League", "Europa League"),
    ("Super Cup", "Super Cup"),
    ("International Match", "International Match"),
)


class Match(models.Model):
    division = models.IntegerField()
    season = models.IntegerField(null=True)
    competition = models.CharField(null=True, max_length=100, choices=match_status)
    home = models.CharField(max_length=30)
    away = models.CharField(max_length=30)
    home_goal = models.IntegerField(null=True, blank=True)
    away_goal = models.IntegerField(null=True, blank=True)
    home_goal_scorer = models.TextField(null=True, blank=True)
    away_goal_scorer = models.TextField(null=True, blank=True)
    date = models.DateTimeField()
    home_lineup = models.TextField(null=True, blank=True)
    away_lineup = models.TextField(null=True, blank=True)
    mom = models.CharField(max_length=30, null=True, blank=True)
    foot_note = models.TextField(null=True, blank=True)
    played = models.BooleanField(default=False, blank=True)
    live = models.BooleanField(default=False, blank=True)



    class Meta:
        verbose_name_plural = 'Matches'

    def __str__(self):
        verbose = f'{self.home} vs {self.away}'
        return verbose


class D1Standing(models.Model):
    season= models.IntegerField(null=True)
    pos = models.IntegerField()
    club = models.CharField(max_length=50)
    mp = models.IntegerField()
    w= models.IntegerField()
    d = models.IntegerField()
    l = models.IntegerField()
    pts = models.IntegerField()

    def __str__(self):
        return self.club


class D2Standing(models.Model):
    season = models.IntegerField(null=True)
    pos = models.IntegerField()
    club = models.CharField(max_length=50)
    mp = models.IntegerField()
    w= models.IntegerField()
    d = models.IntegerField()
    l = models.IntegerField()
    pts = models.IntegerField()

    def __str__(self):
        return self.club


class News(models.Model):
    subject = models.CharField(max_length=1000)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'News'

    def __str__(self):
        return self.subject

class Transfer(models.Model):
    player_name = models.CharField(max_length=50)
    transferred_from = models.CharField(max_length=50)
    transferred_to = models.CharField(max_length=50)
    transferred_price = models.CharField(max_length=50, null=True)
    transferred_date = models.DateField()

    def __str__(self):
        return  self.player_name


class CurrentSeason(models.Model):
    current_season = models.IntegerField()

    class Meta:
        verbose_name_plural = 'Current Season'

    def __str__(self):
        return str(self.current_season)