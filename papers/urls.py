from django.urls import path
from .views import PublicationListView, PublicationDetailView

urlpatterns = [
    path('publications/', PublicationListView.as_view(), name='publication-list'),
    path('publications/<int:pk>/', PublicationDetailView.as_view(),
         name='publication-detail'),
]
