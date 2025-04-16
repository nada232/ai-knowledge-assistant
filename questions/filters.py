from django_filters import rest_framework as filters
from .models import Question

class QuestionFilter(filters.FilterSet):
    question_text = filters.CharFilter(lookup_expr='icontains')
    answer_text = filters.CharFilter(lookup_expr='icontains')
    asked_at_after = filters.DateTimeFilter(field_name='asked_at', lookup_expr='gte')
    asked_at_before = filters.DateTimeFilter(field_name='asked_at', lookup_expr='lte')
    asked_by = filters.NumberFilter(field_name='asked_by__id')
    
    class Meta:
        model = Question
        fields = ['question_text', 'answer_text', 'asked_by', 'asked_at']
