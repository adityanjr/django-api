from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apiREST import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'article', views.ArticleViewSet)
router.register(r'users', views.UserViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]
