from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import *
from .models import *
from rest_framework import views, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissons import *


class PostsViewSets(ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = (IsAuthor,IsAuthenticatedOrReadOnly,)
    
    
    @action(methods=['post'],detail=False)
    def create(self,request):
        ser = PostSerializer(data=request.data)
        if ser.is_valid():
            rq = PostSerializer(Post.objects.create(
                title=request.data['title'],
                desk=request.data['desk'],
                user=request.user,
                cat_id=request.data['cat'],
            ))
        return Response({'object':rq.data},status=status.HTTP_201_CREATED)
    
    @action(methods=['get'],detail=True)
    def CatsSort(self,request,pk):
        return Response({'data':PostSerializer(Post.objects.filter(cat_id=pk),many=True).data},status=status.HTTP_200_OK)
        
    