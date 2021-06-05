from django.urls import path
from .views import (ArticleDetailAPIView, ArticleListCreateAPIView,AuthorListCreateAPIView)

urlpatterns = [
    path("articles/", 
         ArticleListCreateAPIView.as_view(), 
         name="article-list"),

    path("articles/<int:pk>/", 
         ArticleDetailAPIView.as_view(), 
         name="article-detail"),

    path("author/", 
         AuthorListCreateAPIView.as_view(), 
         name="author-list")
    # path("articles/", article_list_create_api_view, name="article-list"),
    # path("articles/<int:pk>/", article_detail_api_view, name="article-detail")
]