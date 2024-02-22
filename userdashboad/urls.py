from django.urls import path
from . views import (
    UserContentListCreateView,
    UserContendUpdateView,
    ContentSearchingView
)
urlpatterns = [
    path('create/content/',UserContentListCreateView.as_view(),name='create_content'),
    path('update/content/<int:pk>/',UserContendUpdateView.as_view(),name='content_update'),
    path('searching/',ContentSearchingView.as_view(),name='content_searching')

]
