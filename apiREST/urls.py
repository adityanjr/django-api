from django.urls import path
from .views import ArticleList, ArticleDetail
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('article/', ArticleList.as_view()),
    path('detail/<int:pk>', ArticleDetail.as_view()),
]
