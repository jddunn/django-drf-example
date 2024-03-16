from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets, generics

from .serializers import GroupSerializer, UserSerializer
from .serializers import ArticleSerializer

from .models import Article

# UI views
def index(request):
    return render(request, 'index.html')

def article_list(request):
    articles = Article.objects.all()
    return render(request, 'example_app/article_list.html', {'articles': articles})

def user_list(request):
    users = User.objects.all()
    return render(request, 'example_app/user_list.html', {'users': users})

# API views
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

# class ArticleList(generics.ListAPIView):
class ArticleList(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer