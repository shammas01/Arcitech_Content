from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser
from useraccount.models import Content
from . serializers import ContentSerializer
from rest_framework.response import Response
from django.http import Http404
from rest_framework import status
# Create your views here.


class AdminContentListView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        if self.request.user.is_staff == True and self.request.user.is_active == True:
            contents = Content.objects.all()
            serializer = ContentSerializer(contents, many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response({"error":"you are not permit to do this action"},status=status.HTTP_400_BAD_REQUEST)
    

class AdminContentManageView(APIView):
    permission_classes = [IsAdminUser]

    def get_object(self, pk):
        try:
            return Content.objects.get(pk=pk)
        except Content.DoesNotExist:
            raise Http404
        
    def get(self, request, pk):
        content = self.get_object(pk)
        serializer = ContentSerializer(content)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        content = self.get_object(pk=pk)
        serializer = ContentSerializer(content,data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        content = self.get_object(pk)
        content.delete()
        return Response({"msg":"successfully deleted"})