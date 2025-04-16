from rest_framework import viewsets, permissions
from .models import Question
from .serializers import QuestionSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters as drf_filters
from .filters import QuestionFilter
from backend.pagination import StandardResultsSetPagination

class QuestionViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = QuestionSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = StandardResultsSetPagination
    filter_backends = [DjangoFilterBackend, drf_filters.SearchFilter, drf_filters.OrderingFilter]
    filterset_class = QuestionFilter
    search_fields = ['question_text', 'answer_text']
    ordering_fields = ['asked_at']
    ordering = ['-asked_at']  # Default ordering
    
    def get_queryset(self):
        return Question.objects.filter(asked_by=self.request.user)
