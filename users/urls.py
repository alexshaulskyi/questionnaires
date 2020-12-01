from django.urls import path, include

from users.views import UserProfile, SignUp


urlpatterns = [
    path('signup/', SignUp.as_view(), name='signup'),
    path('', include("django.contrib.auth.urls")),
    path('profile/<int:pk>/', UserProfile.as_view(), name='user_profile')
]