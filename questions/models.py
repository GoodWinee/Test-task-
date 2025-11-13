from django.db import models

from questions.constants import STR_DISPLAY_LENGTH
from user.models import CustomUser


class Question(models.Model):
    """Модель вопроса."""

    text = models.TextField('Текст вопроса.')
    created_at = models.DateTimeField('Добавлено.', auto_now_add=True)

    def __str__(self) -> str:
        return self.text[:STR_DISPLAY_LENGTH]


class Answer(models.Model):
    """Модель ответа."""

    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        related_name='answers',
        blank=True,
        null=True
    )
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='user_answers',
        blank=True,
        null=True
    )
    text = models.TextField('Текст ответа.')
    created_at = models.DateTimeField('Добавлено.', auto_now_add=True)

    def __str__(self) -> str:
        return self.text[:STR_DISPLAY_LENGTH]
