from rest_framework import serializers

from tests.models import Question, Option, UserPassedTest


class OptionSerializer(serializers.ModelSerializer):

    class Meta:

        model = Question
        fields = ('id', 'text')


class QuestionSerializer(serializers.ModelSerializer):

    options = OptionSerializer(many=True)

    class Meta:

        model = Question
        fields = '__all__'
