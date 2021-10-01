from django.core.files.base import File
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import generic
from main.models import Paper, Author, ResearchGroup
from .filters import PaperFilter
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from main.forms import AddPaperForm, AddAuthorForm
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import get_object_or_404
from django.db.models import Q
from itertools import chain
import requests
from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter 


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


# View class to display PaperUpdate Form, extended from UpdateView class.
class PaperUpdate(PermissionRequiredMixin, UpdateView):
  model = Paper
  permission_required = 'main.can_modify_paper'
  fields = ['name', 'abstract', 'year', 'authors',
            'research_group', 'institution', 'venue', 'pdf', 'peerReview',]

class AuthorUpdate(PermissionRequiredMixin, UpdateView):
  model = Author
  permission_required = 'main.can_modify_author'
  fields = ['name', 'surname', 'papers']


# View class to display AuthorDelete Form, extended from DeleteView class.
class AuthorDelete(PermissionRequiredMixin, DeleteView):
  model = Author
  permission_required = 'main.can_modify_author'
  # If successful deletion, return to author list page.
  success_url = reverse_lazy('authors')


class PaperDelete(PermissionRequiredMixin, DeleteView):
  model = Paper
  permission_required = 'main.can_modify_paper'
  # If successful deletion, return to research paper list page.
  success_url = reverse_lazy('papers')

def report(request):
  # Create Bytestream buffer 
  buf = io.BytesIO()
  # Create a canvas
  c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
  # Create a text object
  textob = c.beginText()
  textob.setTextOrigin(inch, inch)
  textob.setFont('Helvetica', 20)

  # Create blank list
  lines = []
  lines.append("Research Outcome Report ")
  lines.append("The following papers meet the filtering criteria: ")
  lines.append(" ")
  # Designate model
  papers = Paper.objects.all()
  
  for paper in papers:
    lines.append(paper.name)
    lines.append(paper.abstract)
    lines.append(" ")
    

  for line in lines:
    textob.textLine(line)

  c.drawText(textob)
  c.showPage()
  c.save()
  buf.seek(0)

  return FileResponse(buf, as_attachment=True, filename='report.pdf')
