from rest_framework import viewsets, permissions
from .models import Question
from .serializers import QuestionSerializer

class QuestionViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = QuestionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Question.objects.filter(asked_by=self.request.user)