from django.db import models


class Paper(models.Model):
  """This class represents a research paper uploaded to our database, derived from the Model class."""

  name = models.CharField(max_length=100)
  abstract = models.TextField(max_length=500)
  authors = models.ManyToManyField()
  year = models.IntegerField()
  pdf = models.FileField()
  peerReview = models.FileField()
