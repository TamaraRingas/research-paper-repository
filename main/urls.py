from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.urls.conf import include
from . import views


urlpatterns = [
    path('', views.PaperListView.as_view(), name='papers'),
    path('faq/', views.faq_view, name='faq'),
    path('papers/', views.PaperListView.as_view(), name='papers'),
    path('paper/<int:pk>', views.PaperDetailView.as_view(), name='paper-detail'),
    path('authors/', views.AuthorListView.as_view(), name='authors'),
    path('author/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail'),
    path('paper/create/', views.create_paper_view, name='paper_create'),
    path('paper/<int:pk>/update/',
         views.PaperUpdate.as_view(), name='paper_update'),
    path('author/create/', views.create_author_view, name='author_create'),
    path('author/<int:pk>/update/',
         views.AuthorUpdate.as_view(), name='author_update'),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
