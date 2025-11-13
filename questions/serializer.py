from rest_framework import serializers

from questions.models import Answer, Question


class AnswerSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Answer."""

    class Meta:
        model = Answer
        fields = '__all__'

    def validate_text(self, value: str) -> str:
        if not value.strip():
            raise serializers.ValidationError("Текст не может быть пустым.")
        return value


class QuestionSerializer(serializers.ModelSerializer):
    """Сериализер для модели Question."""

    answers: list
    answers = AnswerSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = '__all__'

    def validate_text(self, value: str) -> str:
        if not value.strip():
            raise serializers.ValidationError("Текст не может быть пустым.")
        return value
