from django.urls import include, path
from rest_framework.routers import DefaultRouter

from questions.views import AnswerViewSet, QuestionViewSet

router_v1 = DefaultRouter()
router_v1.register(r'questions', QuestionViewSet)

urlpatterns = [
    path('', include(router_v1.urls)),
    path(
        'questions/<int:question_id>/answers/',
        AnswerViewSet.as_view({'get': 'list', 'post': 'create'}),
        name='question-answers'
    ),
    path(
        'answers/<int:pk>/',
        AnswerViewSet.as_view({'get': 'retrieve', 'delete': 'destroy'}),
        name='answer-detail'
    ),
]