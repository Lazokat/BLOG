from django.urls import path
from .views import *
urlpatterns=[
    path('create/',Create.as_view(),name='create'),
    path('<int:pk>/',Edit.as_view(),name='edit')
]