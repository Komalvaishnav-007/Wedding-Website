from rest_framework import serializers
from .models import Ourguards

class OurGuardsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ourguards
        fields = ['id', 'Ourguards_placename', 'Ourguards_post', 'Ourguards_img']