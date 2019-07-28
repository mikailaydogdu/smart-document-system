from django import forms
from django.contrib.auth.forms import UserCreationForm

from accounts.models import CustomUserTable


class RealDateInput(forms.DateInput):
    input_type = "date"


class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUserTable
        fields = UserCreationForm.Meta.fields + (
            'ident_no', 'email','first_name','last_name', 'birth_date', 'telephone', 'mobile_tel', 'job', 'task', 'image')
        widgets = {"birth_date": RealDateInput}



class UserUpdateForm(forms.ModelForm):
    class Meta(CustomUserTable.Meta):
        model = CustomUserTable
        fields = [
           'ident_no', 'email','first_name','last_name', 'birth_date', 'telephone', 'mobile_tel', 'job', 'task', 'image'
        ]
