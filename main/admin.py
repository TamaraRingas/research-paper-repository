from django.contrib import admin
from .models import Paper, Author, ResearchGroup

# Register your models here.
admin.site.register(Paper)
admin.site.register(Author)
admin.site.register(ResearchGroup)
