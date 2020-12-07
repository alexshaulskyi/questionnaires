from django.urls import path, include
from django.contrib.auth.decorators import login_required
from rest_framework.routers import DefaultRouter

from tests.views import Index, TestView, TestResult
from tests.api_views import GetQuestions, UserPassedTestViewSet

router = DefaultRouter()

router.register('userpassedtest', UserPassedTestViewSet, basename='users')

api_patterns = [
    path('v1/', include(router.urls)),
    path('get_questions/', GetQuestions.as_view(), name='get_questions'),
]

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('api/', include(api_patterns)),
    path('<int:pk>/', login_required(TestView.as_view()), name='single_test'),
    path('test_results/<int:pk>/', TestResult.as_view(), name='test_results'),
]