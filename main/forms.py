from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import models
from django.core import validators
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
import requests
from main.models import Paper, Author

class AddPaperForm(ModelForm):

    def clean_name(self):  # Override clean_data method from ModelForm class.
        data = self.cleaned_data['name']

        if len(data) > 100:  # Check that name entered is valid.
            # If not, raise error.
            raise ValidationError(_('Invalid Paper Name'))
        return data

    # Override clean_data method for the data in each field.
    def clean_abstract(self):
        abstract_data = self.cleaned_data['abstract'] 
        return abstract_data

    def clean_year(self):
        year_data = self.cleaned_data['year']   
        return year_data

    def clean_authors(self):
        authors_data = self.cleaned_data['authors']  
        return authors_data

    def clean_research_group(self):
        research_group_data = self.cleaned_data['research_group']  
        return research_group_data

    def clean_institution(self):
        institution_data = self.cleaned_data['institution']
        return institution_data

    def clean_venue(self):
        venue_data = self.cleaned_data['venue']
        return venue_data

    def clean_pdf(self):
        pdf_data = self.cleaned_data['pdf']
        return pdf_data

    def clean_peer_review(self):
        peer_review_data = self.cleaned_data['peerReview']
        return peer_review_data

    class Meta:
        model = Paper  # Set model class.
        # List which fields are used in form.
        fields = ['name', 'abstract', 'year', 'authors', 'research_group', 'institution', 'venue', 'pdf', 'peerReview' ]
        labels = {  # Set field labels
            'name': 'Name',
            'abstract': 'Abstract',
            'year': 'Year',
            'authors': 'Authors',
            'research_group': 'Research Group',
            'institution': 'Institution',
            'venue': 'Venue',
            'pdf': 'Pdf',
            'peerReview': 'Peer Review',
        }


class AddAuthorForm(forms.ModelForm):
    def clean_name(self):
        data = self.cleaned_data['name']
        return data

    def clean_surname(self):
        surname_data = self.cleaned_data['surname']
        return surname_data

    class Meta:
        model = Author
        fields = ('name', 'surname', )
        labels = {
            'name': 'Name',
            'surname': 'Surname',
        }


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(
        max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(
        max_length=254, help_text='Required. Enter a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',
                  'email', 'password1',)
