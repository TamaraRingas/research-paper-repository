import django_filters
from .models import Paper

class PaperFilter(django_filters.FilterSet):

  class Meta:
    model = Paper
    fields = ('name','abstract', 'year', 'authors', 'research_group', 'institution', 'venue')

  
