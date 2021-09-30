from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import generic
from main.models import Paper, Author, ResearchGroup
from .filters import PaperFilter
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from main.forms import AddPaperForm, AddAuthorForm
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
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


# View class to display PaperCreate Form, extended from CreateView class.

class PaperCreateView(CreateView):
  model = Paper
  fields = ['name', 'abstract', 'year', 'authors',
            'research_group', 'institution', 'venue', 'pdf', 'peerReview']

@login_required
@permission_required('main.can_add_paper')
def create_paper_view(request):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization
    form = AddPaperForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('papers'))

    context['form'] = form
    return render(request, "paper_form.html", context)


@login_required
@permission_required('main.can_add_author')
def create_author_view(request):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization
    form = AddAuthorForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('papers'))

    context['form'] = form
    return render(request, "author_form.html", context)


def update_paper_view(request, id):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # fetch the object related to passed id
    obj = get_object_or_404(Paper, id=id)

    # pass the object as instance in form
    form = AddPaperForm(request.POST or None, instance=obj)

    # save the data from the form and
    # redirect to list of research papers
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("paper-detail.html")

    # add form dictionary to context
    context["form"] = form

    return render(request, "update_paper.html", context)
