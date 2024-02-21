from django.urls import path
from . views import (
    UserContentListCreateView
)
urlpatterns = [
    path('create/content/',UserContentListCreateView.as_view(),name='create_content')
]
