from django.contrib import admin
from .models import Paper, Author, ResearchGroup

"""Models registered here"""
@admin.register(Paper)
class PaperAdmin(admin.ModelAdmin):
  pass

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
  pass
@admin.register(ResearchGroup)
class ResearchGroupAdmin(admin.ModelAdmin):
  pass

