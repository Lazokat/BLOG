from django.shortcuts import render
from rest_framework.generics import *
from .serializers import *
from .models import *

class Create(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
class Edit(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
