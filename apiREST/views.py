from .models import Article
from .serializer import ArticleSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from .serializer import UserSerializer
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly

class ArticleList(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer