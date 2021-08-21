from django.contrib import admin
from .models import Paper, Author, ResearchGroup

"""Models registered here"""
@admin.register(Paper)
class PaperAdmin(admin.ModelAdmin):
  list_display = ('name','display_authors','abstract','year','venue','pdf','peerReview')

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
  pass
@admin.register(ResearchGroup)
class ResearchGroupAdmin(admin.ModelAdmin):
  pass

