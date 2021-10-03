from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import Permission, User
from main.models import Paper, Author, ResearchGroup


class PaperListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create 13 papers for pagination tests
        number_of_papers = 13

        for paper_id in range(number_of_papers):
            Paper.objects.create(
                name=f'TestPaper {paper_id}'
            )

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/main/papers/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        # Use client from TestCase's derived class to simulate a GET request and get a response.
        response = self.client.get(reverse('papers'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        # Use client from TestCase's derived class to simulate a GET request and get a response.
        response = self.client.get(reverse('papers'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/paper_list.html')

    def test_lists_all_papers(self):
        # Get second page and confirm it has (exactly) 3 remaining items
        response = self.client.get(reverse('videos')+'?page=2')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertTrue(len(response.context['paper_list']) == 3)


class PaperDetailViewTest(TestCase):
  @classmethod
  def setUpTestData(cls):
    paper = Paper.objects.create(
        name='TestPaper', abstract='Test paper abstract')
    author1 = Author.objects.create(name='Fabio', surname='Tollon')
    author2 = Author.objects.create(name='Thomas', surname='Meyer')
    paper.authors.add(Author.objects.get(id=1))
    paper.authors.add(Author.objects.get(id=2))

  def test_view_url_exists_at_desired_location(self):
      response = self.client.get('/main/paper/1')
      self.assertEqual(response.status_code, 200)

  def test_view_url_accessible_by_name(self):
      # Use client from TestCase's derived class to simulate a GET request and get a response.
      response = self.client.get(reverse('paper-detail', kwargs={'pk': 1}))
      self.assertEqual(response.status_code, 200)

  def test_view_uses_correct_template(self):
      # Use client from TestCase's derived class to simulate a GET request and get a response.
      response = self.client.get(
          reverse('paper-detail', kwargs={'pk': 1}))
      self.assertEqual(response.status_code, 200)
      self.assertTemplateUsed(response, 'main/paper_detail.html')


class AuthorDetailViewTest(TestCase):
  @classmethod
  def setUpTestData(cls):
    author = Author.objects.create(name='Fabio', surname='Tollon')
    paper = Paper.objects.create(
        name='TestPapr', abstract='Test Paper Abstract', venue='SACJ', year=2021, institution='University of Cape Town', researchGroup='Ethics of AI')
    author.papers.add(Paper.objects.get(id=1))

  def test_view_url_exists_at_desired_location(self):
      response = self.client.get('/main/author/1')
      self.assertEqual(response.status_code, 200)

  def test_view_url_accessible_by_name(self):
      # Use client from TestCase's derived class to simulate a GET request and get a response.
      response = self.client.get(reverse('author-detail', kwargs={'pk': 1}))
      self.assertEqual(response.status_code, 200)

  def test_view_uses_correct_template(self):
      # Use client from TestCase's derived class to simulate a GET request and get a response.
      response = self.client.get(
          reverse('author-detail', kwargs={'pk': 1}))
      self.assertEqual(response.status_code, 200)
      self.assertTemplateUsed(response, 'main/author_detail.html')

class AuthorListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create 13  categories.
        number_of_authors = 2

        for author_id in range(number_of_authors):
            Author.objects.create(
                name=f'TestAuthor {author_id}'
            )

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/main/authors/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        # Use client from TestCase's derived class to simulate a GET request and get a response.
        response = self.client.get(reverse('authors'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        # Use client from TestCase's derived class to simulate a GET request and get a response.
        response = self.client.get(reverse('authors'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/author_list.html')


class LogInTest(TestCase):
  def set_up_data(self):
    self.credentials = {
        'username': 'testuser',
        'password': 'secret'
    }
    User.objects.create_user(**self.credentials)
    response = self.client.post('/login/', self.credentials, follow=True)
    self.assertTrue(response.context['user'].is_active)
