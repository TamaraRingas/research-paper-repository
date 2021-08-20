from django.db import models
from django.urls import reverse


class Paper(models.Model):
    """This class represents a research paper uploaded to our database, derived from the Model class."""

    name = models.CharField(max_length=100)
    abstract = models.TextField(max_length=5000)
    year = models.IntegerField()
    authors = models.ManyToManyField("Author")
    researchGroup = models.ManyToManyField("ResearchGroup", blank=True)
    venue = models.CharField(max_length=300)
    pdf = models.FileField(default=' ', upload_to='media/',
                           verbose_name="Research Paper")
    peerReview = models.FileField(
        default=' ', upload_to='media/', verbose_name="Proof of Peer Review", blank=True)

    # Order reserach papers by year (descending) then by authors.
    class Meta:
        ordering = ['-year']

    def get_absolute_url(self):
        """Returns the url to access a particular research paper."""
        return reverse('paper-detail', args=[str(self.id)])

    def __str__(self):
        """String representation of Paper object"""
        return self.name


class Author(models.Model):
    """This class represents an author, derived from the Model class"""

    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    papers = models.ManyToManyField(Paper, blank=True)
    #researchGroup = models.ManyToManyField()

    # Order authors by their surnames.
    class Meta:
        ordering = ['surname']

    def get_absolute_url(self):
        """Returns the url to access a particular author."""
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        """Formatted string representation of Author object"""
        return f'{self.surname}, {self.name}'


class ResearchGroup(models.Model):
    """This class represents a research group, derived from the Model class."""

    name = models.CharField(max_length=100)
    papers = models.ManyToManyField(Paper,blank=True)
    authors = models.ManyToManyField(Author,blank=True)

    class Meta:
        ordering = ['name']

    def get_absolute_url(self):
        """Returns the url to access a particular research group."""
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        """String representation of ResearchGroup object"""
        return self.name
