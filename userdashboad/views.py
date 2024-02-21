from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from useraccount.models import Content
from admin1.serializers import ContentSerializer
from rest_framework.response import Response
from django.http import Http404
from rest_framework import status

# Create your views here.




class UserContentListCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        contents = Content.objects.filter(user=request.user)
        serializer = ContentSerializer(contents, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)