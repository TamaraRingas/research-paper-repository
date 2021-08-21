from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('papers/', views.PaperListView.as_view(), name='papers'),
    path('paper/<int:pk>', views.PaperDetailView.as_view(), name='paper-detail'),
]
