from django.contrib import admin
from .models import Paper, Author, ResearchGroup

# Register your models here.
@admin.register(Paper)
class PaperAdmin(admin.ModelAdmin):
  pass

admin.site.register(Paper, PaperAdmin)


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
  pass


admin.site.register(Author, AuthorAdmin)


@admin.register(ResearchGroup)
class ResearchGroupAdmin(admin.ModelAdmin):
  pass


admin.site.register(ResearchGroup, ResearchGroupAdmin)
