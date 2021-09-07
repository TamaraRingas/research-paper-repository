from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.PaperListView.as_view(), name='papers'),
    path('faq/', views.faq_view, name='faq'),
    path('papers/', views.PaperListView.as_view(), name='papers'),
    path('paper/<int:pk>', views.PaperDetailView.as_view(), name='paper-detail'),
    path('authors/', views.AuthorListView.as_view(), name='authors'),
    path('author/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
