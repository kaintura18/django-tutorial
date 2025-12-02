from django.db import models

# Create your models here.
class heroname(models.Model):
  herotype_choices = [('warrior', 'Warrior'), ('mage', 'Mage'), ('archer', 'Archer'),('healer', 'Healer')]
  name = models.CharField(max_length=100)
  image= models.ImageField(upload_to='heronames/')

  age = models.IntegerField()
  herotype = models.CharField(max_length=20, choices=herotype_choices )

  def __str__(self):
      return self.name