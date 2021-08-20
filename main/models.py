from django.db import models
from django.urls import reverse


class Paper(models.Model):
    """This class represents a research paper uploaded to our database, derived from the Model class."""

    name = models.CharField(max_length=100)
    abstract = models.TextField(max_length=1000)
    year = models.IntegerField()
    authors = models.ManyToManyField("Author", blank=True)
    #researchGroup = models.ManyToManyField()
    venue = models.CharField(max_length=50)
    pdf = models.FileField(default=' ', upload_to='media/',
                           verbose_name="Research Paper")
    peerReview = models.FileField(
        default=' ', upload_to='media/', verbose_name="Proof of Peer Review")

    # Order reserach papers by year (descending) then by authors.
    class Meta:
        ordering = ['-year']

    def get_absolute_url(self):
        """Returns the url to access a particular research paper."""
        return reverse('paper-detail', args=[str(self.id)])

    def __str__(self):
        return self.name


class Author(models.Model):
    """This class represents an author, derived from the Model class"""

    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    papers = models.ManyToManyField(Paper)
    #researchGroup = models.ManyToManyField()

    # Order authors by their surnames.
    class Meta:
        ordering = ['surname']

    def __str__(self):
        return f'{self.surname}, {self.name}'
