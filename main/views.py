from django.shortcuts import render
from models import Page


# View class that gets and displays video list.
class PageListView(generic.ListView):
    # Inherited from the ListView Class
    model = Page
    paginate_by = 10

    def get_queryset(self):  # Filter results by input query.
      query = self.request.GET.get('query', None)

      if query:
        return Page.objects.filter(name__icontains=query)

      else:
        return Page.objects.all()
