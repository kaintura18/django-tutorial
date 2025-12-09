from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class heroname(models.Model):
  herotype_choices = [('warrior', 'Warrior'), ('mage', 'Mage'), ('archer', 'Archer'),('healer', 'Healer')]
  name = models.CharField(max_length=100)
  image= models.ImageField(upload_to='heronames/')
  age = models.IntegerField()
  herotype = models.CharField(max_length=20, choices=herotype_choices )
  abilities = models.TextField(default='No abilities listed.')

  def __str__(self):
      return self.name
  
class hero_rank(models.Model):
    hero = models.ForeignKey(heroname, on_delete=models.CASCADE)
    rank = models.IntegerField()

    def __str__(self):
        return f"{self.hero.name} - Rank {self.rank}"
  
class association(models.Model):
    name = models.CharField(max_length=100)
    members = models.ManyToManyField(heroname)
    
    def __str__(self):
        return self.name
    