from django.shortcuts import redirect
from django.http.response import JsonResponse
from django.db.models import F, Count
from rest_framework import permissions, status, viewsets
from rest_framework.decorators import action
from rest_framework.views import APIView

from tests.models import Test, UserPassedTest, Question, Option
from tests.serializers import QuestionSerializer, UserPassedTestSerializer


class GetQuestions(APIView):

    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):

        if not request.is_ajax():
            return redirect('index')

        test_id = request.GET.get('test_id')
        test = Test.objects.get(id=test_id)

        obj, created = UserPassedTest.objects.get_or_create(
            user=request.user,
            test=test
        )

        questions = test.questions.all()

        serializer = QuestionSerializer(questions, many=True)

        return JsonResponse(serializer.data, safe=False)


class UserPassedTestViewSet(viewsets.ModelViewSet):

    queryset = UserPassedTest.objects.all()
    serializer_class = UserPassedTestSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=False, methods=['patch'], permission_classes=[permissions.IsAuthenticated])
    def add_option(self, request):

        option_id = request.POST.get('option_id')
        relation_id = request.POST.get('relation_id')

        option = Option.objects.get(id=option_id)
        relation_object = UserPassedTest.objects.get(id=relation_id)

        if not relation_object.questions_answered.filter(id=option.question.id).exists():
            relation_object.questions_answered.add(option.question)
            relation_object.selected_options.add(option)
            relation_object.questions_answered_amount = F('questions_answered_amount') + 1
            relation_object.save()
        else:
            existing_option = relation_object.selected_options.get(question_id=option.question.id)
            relation_object.selected_options.remove(existing_option)
            relation_object.selected_options.add(option)

        return JsonResponse({'success': 'added'})

    @action(detail=False, methods=['patch'], permission_classes=[permissions.IsAuthenticated])
    def set_score(self, request):

        relation_id = request.POST.get('relation_id')

        relation_object = UserPassedTest.objects.get(id=relation_id)

        correct_answers = relation_object.selected_options.filter(is_correct=True).count()
        answers = relation_object.questions_answered_amount

        score = correct_answers / answers
        relation_object.score = score
        relation_object.save()

        return JsonResponse({'success': score})
