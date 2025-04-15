from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from articles.views import ArticleViewSet
from questions.views import QuestionViewSet
from search.views import AskQuestionView, StatsView

# سجل الراوتر
router = DefaultRouter()
router.register(r'articles', ArticleViewSet)
router.register(r'questions', QuestionViewSet, basename='questions')

urlpatterns = [
    path('admin/', admin.site.urls),

    # API routes
    path('api/', include(router.urls)),
    path('api/ask/', AskQuestionView.as_view(), name='ask'),
    path('api/stats/', StatsView.as_view(), name='stats'),

    # Auth routes
    path('api/auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
