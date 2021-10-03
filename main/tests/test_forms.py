from django.test import TestCase
from django.contrib.auth.models import User
from main.forms import *


class AddPaperFormTest(TestCase):
  def test_add_paper_form_name_field(self):
    form = AddPaperForm()
    self.assertTrue(form.fields['name'].label ==
                    None or form.fields['name'].label == 'Paper Name')

  def test_add_paper_form_abstract_field(self):
    form = AddPaperForm()
    self.assertTrue(form.fields['abstract'].label ==
                    None or form.fields['abstract'].label == 'Paper Abstract')

  def test_add_paper_form_year_field(self):
    form = AddPaperForm()
    self.assertTrue(form.fields['year'].label ==
                    None or form.fields['year'].label == 'Paper Year')

  def test_add_paper_form_venue_field(self):
    form = AddPaperForm()
    self.assertTrue(form.fields['venue'].label ==
                    None or form.fields['venue'].label == 'Paper Venue')

  def test_add_paper_form_institution_field(self):
    form = AddPaperForm()
    self.assertTrue(form.fields['institution'].label ==
                    None or form.fields['institution'].label == 'Paper Institution')

  def test_add_paper_form_authors_field(self):
    form = AddPaperForm()
    self.assertTrue(form.fields['authors'].label ==
                    None or form.fields['authors'].label == 'Paper Authors')

  def test_add_paper_form_pdf_field(self):
    form = AddPaperForm()
    self.assertTrue(form.fields['pdf'].label ==
                    None or form.fields['pdf'].label == 'Paper pdf')

  def test_add_paper_form_peer_review_field(self):
    form = AddPaperForm()
    self.assertTrue(form.fields['peer_review'].label ==
                    None or form.fields['peer_review'].label == 'Paper Peer Review')


class AddAuthorFormTest(TestCase):
  def test_add_author_form_name_field(self):
    form = AddAuthorForm()
    self.assertTrue(form.fields['name'].label ==
                    None or form.fields['name'].label == 'Author Name')

  def test_add_author_form_surname_field(self):
    form = AddAuthorForm()
    self.assertTrue(form.fields['surname'].label ==
                    None or form.fields['surname'].label == 'Author Surname')

  def test_add_author_form_papers_field(self):
    form = AddAuthorForm()
    self.assertTrue(form.fields['papers'].label ==
                    None or form.fields['papers'].label == 'Papers')

