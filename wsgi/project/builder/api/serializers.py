from rest_framework import serializers

from ..models import Section, Block, Slide

# Serializers define the API representation.
class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        depth = 1
        fields = ('id', 'name', 'slug', 'order', 'block_set')

class BlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Block
        depth = 1
        fields = ('id', 'name', 'order', 'slide_set', 'title_set', 'paragraph_set', 'image_set', 'button_set')
