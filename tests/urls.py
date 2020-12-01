from django.urls import path, include

from tests.views import Index, TestView, TestResult
from tests.api_views import GetQuestions, SelectOption, CreateUserTestRelation, SetTestCompleted, GetInitialTestStatus


api_patterns = [
    path('get_questions/', GetQuestions.as_view(), name='get_questions'),
    path('add_selected_option/', SelectOption.as_view(), name='select_option'),
    path('create_relation/', CreateUserTestRelation.as_view(), name='create_relation'),
    path('set_completed/', SetTestCompleted.as_view(), name='set_completed'),
    path('get_initial_status/', GetInitialTestStatus.as_view(), name='get_initial_status')
]

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('api/', include(api_patterns)),
    path('<int:pk>/', TestView.as_view(), name='single_test'),
    path('test_results/<int:pk>/', TestResult.as_view(), name='test_results')
]