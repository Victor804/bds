from django.db import models

# Create your models here.
class Team(models.Model):
    color = models.CharField(max_length=200)
    score = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        for player in Player.objects.filter(color=self.color).iterator():
            player.bank += self.score - player.score
            player.score = self.score
            player.save()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.color


class Player(models.Model):
    name= models.CharField(max_length=200)
    color = models.CharField(max_length=200)
    bank = models.IntegerField(default=0)
    score = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        if list(Team.objects.filter(color=self.color)) != []:
            score = Team.objects.filter(color=self.color).get().score
            super().save(*args, **kwargs)
        else:
            return 0

    def __str__(self):
        return self.name
