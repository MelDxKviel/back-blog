from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView, FormView
from django.contrib import messages
from django.urls import reverse_lazy

from .forms import LoginForm, RegistrationForm, ProfileEditForm, ChangePasswordForm


class UserLogin(LoginView):
    redirect_authenticated_user = True
    template_name = 'login.html'
    form = LoginForm

    def get_success_url(self):
        return reverse_lazy('posts')

    def form_invalid(self, form):
        messages.error(self.request, 'Invalid username or password')
        return self.render_to_response(self.get_context_data(form=form))


class UserRegister(CreateView):
    template_name = 'register.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('login')


class ProfileView(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    model = User
    template_name = 'profile.html'


class ProfileEditView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    success_url = '/profile'
    model = User
    template_name = 'profile_edit.html'
    form = ProfileEditForm
    fields = ['username', 'email', ]


class ProfileChangePassword(LoginRequiredMixin, FormView):
    login_url = '/login/'
    success_url = '/profile'
    template_name = 'profile_changepass.html'
    form_class = ChangePasswordForm

    def form_valid(self, form):
        if (self.request.user.check_password(form.cleaned_data["password"])) and (
                form.cleaned_data["password_new1"] == form.cleaned_data["password_new2"]):
            user = User.objects.get(username__exact=self.request.user.username)
            user.set_password(form.cleaned_data["password_new1"])
            user.save()
            return super(ProfileChangePassword, self).form_valid(form)
        else:
            messages.error(self.request, 'Incorrect password')
            return self.render_to_response(self.get_context_data(form=form))

    def form_invalid(self, form):
        messages.error(self.request, 'Required fields are empty')
        return self.render_to_response(self.get_context_data(form=form))


class ProfileDeleteView(LoginRequiredMixin, DeleteView):
    model = User
    success_url = '/posts'
    template_name = 'profile_delete.html'
