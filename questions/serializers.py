from rest_framework import serializers
from .models import Question
from users.serializers import UserSerializer

class QuestionSerializer(serializers.ModelSerializer):
    asked_by = UserSerializer(read_only=True)
    
    class Meta:
        model = Question
        fields = '__all__'
        read_only_fields = ('asked_by', 'asked_at', 'answer_text')
