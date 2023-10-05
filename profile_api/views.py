from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters

from profile_api import permissions
from profile_api import serializer
from profile_api import models


# Create your views here.
class HelloView(APIView):

    def get(self, request,):
        an_api = [
            'Hello API',
            'Finding Serializer',
            'Finding URL',
        ]
        return Response({'message': 'Hello!', 'an_api': an_api})

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_Request
            )
        
    def put(self, request, pk=None):
        return Response({'method':'PUT'})
    
    def patch(self, request, pk=None):
        return Response({'method': 'PATCH'})
    
    def delete(self, request, pk=None):
        return Response({'method': 'DELETE'})
    


class HelloViewSet(viewsets.ViewSet):
    serializer_class = serializer.HelloSerializer

    def list(self, request):
        a_viewset = [
             'Hello API',
            'Finding Serializer',
            'Finding URL',
        ]
        return Response({'message' : 'Hello!', 'a_viewset': a_viewset})
    
    def create(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message' : message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_404_BAD_REQUEST
            )
        
    def retrieve(self, request, pk=None):
        return Response({'http_method' : 'GET'})
    
    def update(self, request, pk=None):
        return Response({'http_method':'PUT'})
    
    def partial_update(self, request, pk=None):
        return Response({'http_method':'PATCH'})
    
    def destroy(self, request, pk=None):
        return Response({'http_method':'DELETE'})
    


class UserProfileViewSet(viewsets.ModelViewSet):
    serializer_class = serializer.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)
    

