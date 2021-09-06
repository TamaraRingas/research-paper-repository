from os import name
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
class Author(models.Model):
    """This class represents an author, derived from the Model class"""

    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    researchGroup = models.ForeignKey('ResearchGroup', on_delete=models.SET_NULL, null=True)
    institution = models.CharField(max_length=100, blank=True)
    #papers = models.ManyToManyField('Paper', blank=True)
    # Order authors by their surnames.
    class Meta:
        ordering = ['surname']

    def get_absolute_url(self):
        """Returns the url to access a particular author."""
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        """Formatted string representation of Author object"""
        return f'{self.surname}, {self.name}'

    def ordered_authors(self):
        "Return an ordered set of authors"
        return self.authors.all().order_by('surname')

class ResearchGroup(models.Model):
    """This class represents a research group, derived from the Model class."""

    name = models.CharField(max_length=100)

    class Meta:
        ordering = ['name']

    def get_absolute_url(self):
        """Returns the url to access a particular research group."""
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        """String representation of ResearchGroup object"""
        return self.name



class Paper(models.Model):
    """This class represents a research paper uploaded to our database, derived from the Model class."""

    name = models.CharField(max_length=100)
    abstract = models.TextField(max_length=5000)
    year = models.IntegerField()
    authors = models.ManyToManyField(Author)
    research_group = models.CharField(max_length=500, null = True, blank=True)
    institution = models.CharField(max_length=100, blank=True)
    venue = models.CharField(max_length=300)
    pdf = models.FileField(default=' ', upload_to='media/',
                           verbose_name="Research Paper")
    peerReview = models.FileField(
        default=' ', upload_to='media/', verbose_name="Proof of Peer Review", blank=True)
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True)

    # Order reserach papers by year (descending) then by authors.
    class Meta:
        ordering = ['-year']
        #order_with_respect_to = 'year', 'authors'

    def get_absolute_url(self):
        """Returns the url to access a particular research paper."""
        return reverse('paper-detail', args=[str(self.id)])

    def __str__(self):
        """String representation of Paper object"""
        return self.name

    def display_authors(self):
      """Create a string for the Authors. This is required to display authors in Admin."""
      return ', '.join(authors.surname for authors in self.authors.all()[:3])

    
