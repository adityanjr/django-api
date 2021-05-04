from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import ArticleList, ArticleDetail, UserList, UserDetail, api_root, ArticleHighlight


# API endpoints
urlpatterns = format_suffix_patterns([
    path('', api_root),
    path('articles/',
         ArticleList.as_view(),
         name='article-list'),
    path('articles/<int:pk>/',
         ArticleDetail.as_view(),
         name='article-detail'),
    path('articles/<int:pk>/highlight/',
         ArticleHighlight.as_view(),
         name='article-highlight'),
    path('users/',
         UserList.as_view(),
         name='user-list'),
    path('users/<int:pk>/',
         UserDetail.as_view(),
         name='user-detail')
])
