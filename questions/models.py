from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Question(models.Model):
    question_text = models.TextField()
    answer_text = models.TextField()
    asked_at = models.DateTimeField(auto_now_add=True)
    asked_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.question_text[:50]
