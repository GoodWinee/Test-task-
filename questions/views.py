from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

from questions.models import Answer, Question
from questions.serializer import AnswerSerializer, QuestionSerializer


class QuestionViewSet(viewsets.ModelViewSet):
    """Вьюсет для работы с вопросами."""

    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    pagination_class = PageNumberPagination


class AnswerViewSet(viewsets.ModelViewSet):
    """Вьюсет для работы с ответами."""

    serializer_class = AnswerSerializer
    queryset = Answer.objects.all()

    def get_question(self) -> Question:
        """Возвращаем вопрос по question_id."""
        question_id = self.kwargs.get('question_id')
        return get_object_or_404(Question, pk=question_id)

    def get_queryset(self):
        """Возвращаем ответы для конкретного вопроса."""
        question = self.get_question()
        return question.answers.all()

    def perform_create(self, serializer: AnswerSerializer) -> None:
        """Создаём ответ, связывая его с вопросом."""
        question = self.get_question()
        serializer.save(question=question)
