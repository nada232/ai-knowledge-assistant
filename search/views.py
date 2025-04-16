import openai
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from django.conf import settings
from articles.models import Article
from questions.models import Question
from rest_framework.pagination import PageNumberPagination

class AskQuestionView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def post(self, request):
        question_text = request.data.get('question')
        if not question_text:
            return Response({'error': 'Question text is required'}, status=status.HTTP_400_BAD_REQUEST)
        
        # Get relevant articles (simple keyword matching for this example)
        articles = Article.objects.filter(content__icontains=question_text)[:3]
        context = "\n\n".join([f"Article: {a.title}\n{a.content}" for a in articles])
        
        # Call OpenAI API
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful knowledge assistant. Answer the question based on the following context."},
                    {"role": "user", "content": f"Context:\n{context}\n\nQuestion: {question_text}"}
                ],
                temperature=0.7,
            )
            answer_text = response.choices[0].message.content
            
            # Save question and answer
            question = Question.objects.create(
                question_text=question_text,
                answer_text=answer_text,
                asked_by=request.user
            )
            
            return Response({'answer': answer_text})
        
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class StatsView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request):
        # Get paginated recent questions
        paginator = PageNumberPagination()
        paginator.page_size = 5
        recent_questions = Question.objects.order_by('-asked_at')
        result_page = paginator.paginate_queryset(recent_questions, request)
        
        stats = {
            'article_count': Article.objects.count(),
            'question_count': Question.objects.count(),
            'recent_questions': [{
                'question_text': q.question_text,
                'asked_at': q.asked_at
            } for q in result_page]
        }
        
        return paginator.get_paginated_response(stats)
