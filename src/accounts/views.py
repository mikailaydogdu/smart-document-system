from django.urls import reverse_lazy
from django.views.generic import CreateView
from accounts import forms


class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('home')
    template_name = "accounts/signup.html"