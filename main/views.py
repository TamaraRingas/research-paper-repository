from django.shortcuts import render, redirect
from django.views import generic
from main.models import Paper, Author, ResearchGroup
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
    return render(request, 'index.html', context=context)
