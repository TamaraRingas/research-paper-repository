from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('faq/', views.faq_view, name='faq'),
    path('papers/', views.PaperListView.as_view(), name='papers'),
    path('paper/<int:pk>', views.PaperDetailView.as_view(), name='paper-detail'),
    path('authors/', views.AuthorListView.as_view(), name='authors'),
    path('author/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail'),
]
