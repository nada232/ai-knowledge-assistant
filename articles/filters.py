from django_filters import rest_framework as filters
from articles.models import Article

class ArticleFilter(filters.FilterSet):
    title = filters.CharFilter(field_name='title', lookup_expr='icontains')
    content = filters.CharFilter(field_name='content', lookup_expr='icontains')
    tags = filters.CharFilter(field_name='tags', lookup_expr='icontains')
    created_at_after = filters.DateTimeFilter(field_name='created_at', lookup_expr='gte')
    created_at_before = filters.DateTimeFilter(field_name='created_at', lookup_expr='lte')
    author = filters.NumberFilter(field_name='author__id')

    class Meta:
        model = Article
        fields = ['title', 'content', 'tags', 'author', 'created_at']
