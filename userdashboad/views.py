from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated,AllowAny
from useraccount.models import Content
from admin1.serializers import ContentSerializer
from rest_framework.response import Response
from django.http import Http404
from rest_framework import status
from django.db.models import Q 

# Create your views here.




class UserContentListCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        contents = Content.objects.filter(user=request.user)
        serializer = ContentSerializer(contents, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def post(self, request):
        user = request.user
        request.data['user'] = user.id
        serializer = ContentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"plan purchase successfully"},status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserContendUpdateView(APIView):
    permission_classes = [IsAuthenticated]

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
    

class ContentSearchingView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        q = request.GET.get('q')
        Q_base = Q()
        if q:
            Q_base = Q(title__icontains=q) | Q(body__icontains=q) | Q(summary__icontains=q) | Q(categories__name__icontains=q)
        contents = Content.objects.filter(Q_base).distinct()
        serializer = ContentSerializer(contents, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)