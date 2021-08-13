from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import MahasiswaModel


class MahasiswaForm(forms.ModelForm):

    class Meta:
        model = MahasiswaModel
        fields = (
            "nama",
            "nim",
            "kelas",
            "jurusan",
            "shift",
        )

        widgets = {
            'nama': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'masukan nama',
                }
            ),

            'nim': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'masukan nim',
                }
            ),

            'kelas': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'masukan kelas',
                }
            ),

            'jurusan': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),

            'shift': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
        }


class RegisterUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(
                attrs={
                    'class': 'fadeIn second',
                    'placeholder': 'Username...',
                }
            ),
            'email': forms.TextInput(
                attrs={
                    'class': 'fadeIn second',
                    'placeholder': 'Email...',
                }
            ),
            'password1': forms.PasswordInput(
                attrs={
                    'class': 'fadeIn second',
                    'placeholder': 'Email...',
                }
            ),
            'password2': forms.PasswordInput(
                attrs={
                    'class': 'fadeIn second',
                    'placeholder': 'Email...',
                }
            ),
        }
