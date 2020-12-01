from django.shortcuts import render
from django.views.generic import ListView, DetailView, View
from django.shortcuts import redirect
from rest_framework import permissions, generics, views

from tests.models import Test, Question, UserPassedTest
from tests.serializers import QuestionSerializer


class Index(ListView):

    model = Test
    template_name = 'index.html'


class TestView(DetailView):

    model = Test
    template_name = 'single_test.html'


class TestResult(View):

    def get(self, request, pk):

        obj = UserPassedTest.objects.get(
            user=request.user,
            test=Test.objects.get(id=pk)
        )

        options = obj.selected_options.all()
        score = obj.score

        return render(request, 'test_results.html', {'options': options, 'score': score})