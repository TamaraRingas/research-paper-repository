from django.shortcuts import render, redirect
from django.views import generic
from main.models import Paper, Author, ResearchGroup
from .filters import PaperFilter
from django.db.models import Q
from itertools import chain
import requests


def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_papers = Paper.objects.all().count()
    num_authors = Author.objects.all().count()
    num_research_groups = ResearchGroup.objects.all().count()

    context = {
        'num_papers': num_papers,
        'num_authors': num_authors,
        'num_research_groups': num_research_groups,
        
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'paper_list.html', context=context)


def faq_view(request):
  return render(request, 'faq.html')

class PaperListView(generic.ListView):
    model = Paper
    author_list = Author.objects.all()

    def get_queryset(self):  # Filter results by input query.
      query = self.request.GET.get('query', None)
      
      if query:
        return Paper.objects.filter(name__icontains=query) | Paper.objects.filter(venue__icontains=query) | Paper.objects.filter(year__contains=query) | Paper.objects.filter(institution__icontains=query) | Paper.objects.filter(research_group__icontains=query) | Paper.objects.filter(authors__name__icontains=query) | Paper.objects.filter(authors__surname__icontains=query)

      else:
        return Paper.objects.all()

    def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context['filter'] = PaperFilter(self.request.GET, queryset=self.get_queryset())
      return context 

class PaperDetailView(generic.DetailView):
  model = Paper


class AuthorListView(generic.ListView):
    model = Author
    #paginate_by = 20

    def get_queryset(self):  # Filter results by input query.
      query = self.request.GET.get('query', None)

      if query:
        return Author.objects.filter(surname__icontains=query) | Author.objects.filter(name__icontains=query)
        

      else:
        return Author.objects.all()



class AuthorDetailView(generic.DetailView):
  model = Author
