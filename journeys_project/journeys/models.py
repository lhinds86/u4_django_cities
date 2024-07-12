from django.db import models

# Create your models here.

class City(models.Model):
  name = models.CharField(max_length = 100)
  state = models.CharField(max_length = 100)
  description = models.TextField()

  def __str__(self):
    return self.name
  
class Attraction(models.Model):
  city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='attractions')
  name = models.CharField(max_length=100, default = 'no name')
  description = models.TextField()
  image_url = models.CharField(max_length=500, null=True)

  def __str__(self):
    return self.name
    
class Review(models.Model):
  attraction = models.ForeignKey(Attraction, on_delete=models.CASCADE, related_name='reviews')
  rating = models.IntegerField()
  comment = models.TextField()

  def __str__(self):
    return f'Review for {self.attraction.name} - {self.rating} stars'