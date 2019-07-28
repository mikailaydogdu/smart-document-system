from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView
from accounts.forms import RegisterForm, UserUpdateForm
from accounts.models import CustomUserTable


class RegisterView(CreateView):
    form_class = RegisterForm
    model = CustomUserTable
    template_name = 'accounts/usertable_form.html'
    success_url = "/admin"


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = CustomUserTable
    form_class = UserUpdateForm
    template_name = 'accounts/usertable_form.html'

    def get_success_url(self):
        return reverse_lazy("me")

    def get_object(self, queryset=None):
        return self.request.user


class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = CustomUserTable
    context_object_name = 'user_detail'
    template_name = 'accounts/usertable_detail.html'
    is_me = False

    def get_object(self, queryset=None):
        if self.is_me:
            return self.request.user
        else:
            return super().get_object(queryset)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["is_me"] = self.is_me
        return context
