from django.db import models


class Paper(models.Model):
    """This class represents a research paper uploaded to our database, derived from the Model class."""

    name = models.CharField(max_length=100)
    abstract = models.TextField(max_length=1000)
    year = models.IntegerField()
    authors = models.ManyToManyField()
    researchGroup = models.ManyToManyField()
    venue = models.CharField()
    pdf = models.FileField(default=' ', upload_to='media/',
                           verbose_name="Research Paper")
    peerReview = models.FileField(
        default=' ', upload_to='media/', verbose_name="Peer Review")

    class Meta:
        ordering = ['-year', 'authors']

    def __str__(self):
        return self.name
