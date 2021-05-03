from django.urls import path, include
from .views import ArticleList, ArticleDetail, UserList, UserDetail

urlpatterns = [
    path('article/', ArticleList.as_view()),
    path('detail/<int:pk>', ArticleDetail.as_view()),
    path('users/', UserList.as_view()),
    path('users/<int:pk>/', UserDetail.as_view()),
]

urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]