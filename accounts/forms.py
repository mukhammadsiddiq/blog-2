from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserCreation(UserCreationForm):
    class Meta:
        models = CustomUser
        fields = ('username', 'first_name', 'last_name', 'age')


class CustomChangeCreation(UserChangeForm):
    class Meta:
        models = CustomUser
        fields = ('username', 'first_name', 'last_name', 'age')