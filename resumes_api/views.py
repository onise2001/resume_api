from django.shortcuts import render
from .models import Resume
from .serializers import ResumeSerializer
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from drf_yasg.utils import swagger_auto_schema
from resumes.yasg import CustomAutoSchema
# Create your views here.

#@swagger_auto_schema(auto_schema=CustomAutoSchema)
class ResumeViewSet(GenericViewSet):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer
    #parser_classes = (MultiPartParser, FormParser)


    def list(self, request):
        queryset = Resume.objects.all()

        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    def create(self,request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def retrieve(self, request, pk=None):
        instance = self.get_object()
        if instance:
            serializer = self.serializer_class(instance)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)

    
    def destroy(self, request, pk=None):
        instance = self.get_object()
        if instance:
            instance.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    def update(self, request, pk=None):
        instance = self.get_object()
        if instance:
            serializer = self.serializer_class(instance=instance, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response(status=status.HTTP_404_NOT_FOUND)
     
    
    
    