from django.shortcuts import redirect
from django.http.response import JsonResponse
from django.db.models import F, Count
from rest_framework import permissions, status
from rest_framework.views import APIView

from tests.models import Test, UserPassedTest, Question, Option
from tests.serializers import QuestionSerializer


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


class CreateUserTestRelation(APIView):

    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):

        test_id = request.POST.get('test_id')
        test = Test.objects.get(id=test_id)
        
        obj, created = UserPassedTest.objects.get_or_create(
            user=request.user,
            test=test
        )

        if created:
            return JsonResponse({'success': 'created'}, status=status.HTTP_201_CREATED)
        return JsonResponse({'error': 'already exists'}, status=status.HTTP_400_BAD_REQUEST)


class SelectOption(APIView):

    def post(self, request):

        option_id = request.POST.get('option_id')
        test_id = request.POST.get('test_id')

        test = Test.objects.get(id=test_id)
        option = Option.objects.get(id=option_id)

        relation_object = UserPassedTest.objects.get(
            user=request.user,
            test=test
        )

        if not relation_object.questions_answered.filter(id=option.question.id).exists():
            relation_object.questions_answered.add(option.question)
            relation_object.selected_options.add(option)
            UserPassedTest.objects.filter(
                user=request.user,
                test=test
            ).update(
                questions_answered_amount=F('questions_answered_amount') + 1
            )
        else:
            existing_option = relation_object.selected_options.get(question_id=option.question.id)
            relation_object.selected_options.remove(existing_option)
            relation_object.selected_options.add(option)

        return JsonResponse({'success': 'added'})


class SetTestCompleted(APIView):

    def post(self, request):

        test_id = request.POST.get('test_id')
        test = Test.objects.get(id=test_id)

        obj = UserPassedTest.objects.get(user=request.user, test=test)

        correct_answers = obj.selected_options.filter(is_correct=True).count()
        answers = obj.questions_answered_amount

        score = round(correct_answers / answers, 2)

        obj.is_completed = True
        obj.score = score
        obj.save()
        
        return JsonResponse({'success': correct_answers})


class GetInitialTestStatus(APIView):

    def get(self, request):

        test_id = request.GET.get('test_id')
        test = Test.objects.get(id=test_id)

        obj = UserPassedTest.objects.get(user=request.user, test=test)

        return JsonResponse(
            {
            'is_completed': obj.is_completed,
            'start_from_question': obj.questions_answered_amount,
            }
        )