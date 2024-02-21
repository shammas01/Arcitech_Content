from django.urls import path
from . views import (
    AdminContentListView,
    AdminContentManageView
)

urlpatterns = [
    path('contents/',AdminContentListView.as_view(),name='list_contents'),
    path('update/content/<int:pk>/',AdminContentManageView.as_view(),name='update_content')
]