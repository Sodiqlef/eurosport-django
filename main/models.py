from django.db import models
from cloudinary.models import CloudinaryField

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
    edition = models.IntegerField(null=True)
    image = CloudinaryField('image', null=True)
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
        verbose = f'{self.home} vs {self.away} --- {self.edition}'
        return verbose


class D1Standing(models.Model):
    edition= models.IntegerField(null=True)
    club = models.CharField(max_length=50)
    image = CloudinaryField('image', null=True)
    mp = models.IntegerField()
    w= models.IntegerField()
    d = models.IntegerField()
    l = models.IntegerField()
    pts = models.IntegerField()

    def __str__(self):
        return f'{self.club} --- {self.edition}'


class D2Standing(models.Model):
    edition = models.IntegerField(null=True)
    club = models.CharField(max_length=50)
    image = CloudinaryField('image', null=True)
    mp = models.IntegerField()
    w= models.IntegerField()
    d = models.IntegerField()
    l = models.IntegerField()
    pts = models.IntegerField()

    def __str__(self):
        return f'{self.club} --- {self.edition}'


class News(models.Model):
    subject = models.CharField(max_length=1000)
    body = models.TextField()
    image = CloudinaryField('image', null=True)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'News'

    def __str__(self):
        return self.subject

class Transfer(models.Model):
    player_name = models.CharField(max_length=50)
    image = CloudinaryField('image', null=True)
    transferred_from = models.CharField(max_length=50)
    transferred_to = models.CharField(max_length=50)
    transferred_price = models.CharField(max_length=50, null=True)
    transferred_date = models.DateField()

    def __str__(self):
        return  self.player_name

class Club(models.Model):
    division = models.IntegerField(null=True)
    name = models.CharField(max_length=50)
    players = models.TextField()
    highest_goal_scorer = models.CharField(max_length=50)
    current_goals_scored = models.IntegerField()
    all_goals_scored = models.IntegerField(max_length=50, null=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return  self.player_name


class Player(models.Model):
    name = models.CharField(max_length=50)
    club = models.CharField(max_length=50)
    image = CloudinaryField('image', null=True)
    current_goals = models.IntegerField(null=True)
    total_goals = models.IntegerField(null=True)
    current_assists = models.IntegerField(null=True)
    total_assists = models.IntegerField(null=True)
    edition_joined = models.IntegerField(blank=True, null=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Currentedition(models.Model):
    current_edition = models.IntegerField()

    class Meta:
        verbose_name_plural = 'Current edition'

    def __str__(self):
        return str(self.current_edition)