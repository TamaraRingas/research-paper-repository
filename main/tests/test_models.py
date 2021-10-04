from main.models import ResearchGroup
from django.test import TestCase
from models import Paper, Author, ResearchGroup


class ResearchGroupModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        ResearchGroup.objects.create(name='Ethics of AI')

        def test_research_group_name(self):
            research_group = ResearchGroup.objects.get(id=1)
            field_label = research_group._meta.get_field('name').verbose_name
            self.assertEquals(field_label, 'name')


class AuthorModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Author.objects.create(name='Fabio')
        Author.objects.create(surname='Tollon')
        Author.objects.create(
            papers='Artifacts and affordances: from designed properties to possibilities for action')

        def test_author_name(self):
            author = Author.objects.get(id=1)
            field_label = author._meta.get_field('name').verbose_name
            self.assertEquals(field_label, 'name')

        def test_author_surname(self):
            author = Author.objects.get(id=1)
            field_label = author._meta.get_field('surname').verbose_name
            self.assertEquals(field_label, 'surname')

        def test_author_researchGroup(self):
            author = Author.objects.get(id=1)
            field_label = author._meta.get_field('researchGroup').verbose_name
            self.assertEquals(field_label, 'researchGroup')

        def test_author_instituttion(self):
            author = Author.objects.get(id=1)
            field_label = author._meta.get_field('institution').verbose_name
            self.assertEquals(field_label, 'institution')

        def test_author_papers(self):
            author = Author.objects.get(id=1)
            author.papers.add(Author.objects.get(id=1))
            count = Paper.objects.count()
            self.assertEquals(count, 1)

        def test_get_absolute_url(self):
            author = Author.objects.get(id=1)
            # This will also fail if the urlconf is not defined.
            # Check that url for research paper is correct.
            self.assertEquals(author.get_absolute_url(), '/main/authors/1')


class PaperModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Paper.objects.create(
            name='Artifacts and affordances: from designed properties to possibilities for action')
        Paper.objects.create(abstract='In this paper I critically evaluate the value neutrality thesis regarding technology, and find it wanting. I then introduce the various ways in which artifacts can come to influence moral value, and our evaluation of moral situations and actions. Here, following van de Poel and Kroes, I introduce the idea of value sensitive design. Specifically, I show how by virtue of their designed properties, artifacts may come to embody values. Such accounts, however, have several shortcomings. In agreement with Michael Klenk, I raise epistemic and metaphysical issues with respect to designed properties embodying value. The concept of an affordance, borrowed from ecological psychology, provides a more philosophically fruitful grounding to the potential way(s) in which artifacts might embody values. This is due to the way in which it incorporates key insights from perception more generally, and how we go about determining possibilities for action in our environment specifically. The affordance account as it is presented by Klenk, however, is insufficient. I therefore argue that we understand affordances based on whether they are meaningful, and, secondly, that we grade them based on their force.')
        Paper.objects.create(year=2021)
        Author.objects.create(name='Fabio')
        Author.objects.create(surname='Tollon')
        Paper.objects.create(research_group='Ethics of AI')
        Paper.objects.create(institution='University of Pretoria')
        Paper.objects.create(
            venue='AI SOCIETY Journal of Knowledge, Culture and Communication')
        # pdf

    def test_paper_name(self):
        paper = Paper.objects.get(id=1)
        field_label = paper._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_name_max_length(self):
        paper = Paper.objects.get(id=1)
        max_length = paper._meta.get_field('name').max_length
        self.assertEquals(max_length, 100)

    def test_paper_abstract(self):
        paper = Paper.objects.get(id=1)
        field_label = paper._meta.get_field('abstract').verbose_name
        self.assertEquals(field_label, 'abstract')

    def test_paper_year(self):
        paper = Paper.objects.get(id=1)
        field_label = paper._meta.get_field('year').verbose_name
        self.assertEquals(field_label, 'year')

    def test_paper_research_group(self):
        paper = Paper.objects.get(id=1)
        field_label = paper._meta.get_field('research_group').verbose_name
        self.assertEquals(field_label, 'research_group')

    def test_paper_institution(self):
        paper = Paper.objects.get(id=1)
        field_label = paper._meta.get_field('institution').verbose_name
        self.assertEquals(field_label, 'institution')

    def test_paper_abstract(self):
        paper = Paper.objects.get(id=1)
        field_label = paper._meta.get_field('venue').verbose_name
        self.assertEquals(field_label, 'venue')

    def test_paper_authors(self):
        paper = Paper.objects.get(id=1)
        paper.authors.add(Author.objects.get(id=1))
        count = Author.objects.count()
        self.assertEquals(count, 1)

    def test_get_absolute_url(self):
        paper = Paper.objects.get(id=1)
        # This will also fail if the urlconf is not defined.
        # Check that url for research paper is correct.
        self.assertEquals(paper.get_absolute_url(), '/main/papers/1')
