from rest_framework import generics
from ourguardsnew.models import Ourguards
from .serializers import OurGuardsSerializer

class OurGuardsListCreateAPIView(generics.ListCreateAPIView):
    queryset = Ourguards.objects.all()
    serializer_class = OurGuardsSerializer


class OurGuardsRetrieveUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ourguards.objects.all()
    serializer_class = OurGuardsSerializer