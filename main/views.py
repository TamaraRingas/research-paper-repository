from django.shortcuts import render, redirect
from django.views import generic
from main.models import Page
import requests


# View class that displays Video Details.
class PageDetailView(generic.DetailView):
    # Extended from the DetailView class.
    model = Page  # Gets data from the Page model.


# View class that gets and displays list of research papers.
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


"""# View method to use signup form and display it to the user.
def signup_view(request):
    # Set the html form that will post user inputs.
    form = UserCreationForm(request.POST)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        # Set up & authenticate user.
        user = authenticate(username=username, password=password)
        login(request, user)  # Log user in after authentication.
        return redirect('index')  # Then take them to the home page.
    # Display the output to the UI View.
    return render(request, 'signup.html', {'form': form})"""

"""def faq_view(request):
  return render(request, 'faq.html')"""
