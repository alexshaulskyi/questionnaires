from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, View, TemplateView

from users.models import User, NotifySuperuser
from users.forms import SignUpForm, EditProfileForm
from tests.models import UserPassedTest


class SignUp(CreateView):

    template_name = 'signup.html'
    form_class = SignUpForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):

        raw_password = form.instance.password
        form.instance.set_password(raw_password)

        return super().form_valid(form)

class UserProfile(DetailView):

    model = User

    def get_context_data(self, **kwargs):
        context = super(UserProfile, self).get_context_data(**kwargs)
        context['notificator'] = NotifySuperuser.objects.filter(id=1).exists()
        context['tests'] = UserPassedTest.objects.filter(user=self.request.user)
        return context

    def get_template_names(self):

        if self.request.user.is_superuser or self.request.user.is_staff:
            return 'profile_teacher.html'
        return 'profile.html'


class ProfileEdit(UpdateView):

    template_name = 'profile_edit.html'
    form_class = EditProfileForm
    model = User
    
    def get_success_url(self):
        return reverse_lazy('user_profile', kwargs={'pk': self.request.user.pk})
