from django.urls import path
from .views_api import (
    OurGuardsListCreateAPIView,
    OurGuardsRetrieveUpdateDeleteAPIView
)

urlpatterns = [
    path('ourguards/', OurGuardsListCreateAPIView.as_view(), name='ourguards-list'),
    path('ourguards/<int:pk>/', OurGuardsRetrieveUpdateDeleteAPIView.as_view(), name='ourguards-detail'),
]