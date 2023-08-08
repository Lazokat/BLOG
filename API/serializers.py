from rest_framework.serializers import ModelSerializer
from .models import *
class PostSerializer(ModelSerializer):
    class Meta:
        fields='__all__'
        model=Post
