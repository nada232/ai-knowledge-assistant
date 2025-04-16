from rest_framework import viewsets, permissions, filters as drf_filters
from .models import Article
from .serializers import ArticleSerializer
from backend.pagination import StandardResultsSetPagination

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    pagination_class = StandardResultsSetPagination
    filter_backends = [drf_filters.SearchFilter, drf_filters.OrderingFilter]
    
    # هنستخدم search بدل filterset
    search_fields = ['title', 'content', 'tags']
    ordering_fields = ['created_at', 'updated_at']
    ordering = ['-created_at']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
