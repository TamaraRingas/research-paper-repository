from django.db import models


class Paper(models.Model):
  """This class represents a research paper uploaded to our database, derived from the Model class."""

  name = models.CharField(max_length=100)
  abstract = models.CharField(max_length=250)
  year = models.IntegerField()
  peerReview = models.FileField()
