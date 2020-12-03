from django.urls import path, include

from users.views import UserProfile, SignUp, ProfileEdit


urlpatterns = [
    path('', include("django.contrib.auth.urls")),
    path('signup/', SignUp.as_view(), name='signup'),
    path('profile/<int:pk>/', UserProfile.as_view(), name='user_profile'),
    path('edit_profile/<int:pk>/', ProfileEdit.as_view(), name='profile_edit')
]