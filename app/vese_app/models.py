from django.db import models

# Create your models here.

class League(models.Model):
    name = models.CharField(max_length=255,unique=True)
    name_short = models.CharField(max_length=10,unique=True)

    def __str__(self):
        return self.name


class Season(models.Model):
    number = models.IntegerField('Season', primary_key=True)
    start_date = models.DateField('Season Start')
    end_date = models.DateField('Season End')
    leagues = models.ManyToManyField(League)

    def __str__(self):
        return "Season " + str(self.number)


class Team(models.Model):
    name = models.CharField(max_length=50, unique=True)
    name_short = models.CharField(max_length=10, unique=True)
    def __str__(self):
            return self.name


class Player(models.Model):
    name = models.CharField(max_length=255, unique=True)
    discord_name = models.CharField('Discord', max_length=255, unique=True, blank=True, null=True)
    steam_link = models.CharField('Steam', max_length=255, unique=True, blank=True, null=True)
    streamer_link = models.CharField('Stream URL', max_length=255, unique=True, blank=True, null=True)
    league = models.ForeignKey(League, on_delete=models.PROTECT)
    team = models.ForeignKey(Team, blank=True, null=True, on_delete=models.SET_NULL)
    is_captain = models.BooleanField(default=False)
    is_general_manager = models.BooleanField(default=False)
    is_assistant_general_manager = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Week(models.Model):
    number = models.IntegerField('Week', primary_key=True)
    season = models.ForeignKey(Season, on_delete=models.PROTECT)

    def __str__(self):
        return "Week " + str(self.number)


class Series(models.Model):
    week = models.ForeignKey(Week, on_delete=models.CASCADE)
    home_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='home')
    away_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='away')
    home_players = models.ManyToManyField(Player, blank=True, related_name='home_players') # need to filter for only players on that team
    away_players = models.ManyToManyField(Player, blank=True, related_name='away_players') # need to filter for only players on that team
    winner = models.ForeignKey(Team, blank=True, null=True, on_delete=models.SET_NULL, related_name='series_winning_team')
    
    def __str__(self):
        return str(self.week) + ": " + str(self.away_team) + " v " + str(self.home_team)


class Game(models.Model):
    number = models.IntegerField('game', primary_key=True)
    series = models.ForeignKey(Series, on_delete=models.CASCADE)
    winner = models.ForeignKey(Team, blank=True, null=True, on_delete=models.SET_NULL, related_name='game_winning_team')
    
    




