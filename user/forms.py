from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm


class UserCreateForm(UserCreationForm):

    class Meta:
        model = get_user_model()
        fields = ("first_name", "last_name", "email", "password1", "password2")


class UserUpdateForm(ModelForm):

    class Meta:
        model = get_user_model()
        fields = ("first_name", "last_name", "email")
