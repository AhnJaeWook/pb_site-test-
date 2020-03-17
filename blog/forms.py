from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import Blog
from ckeditor_uploader.widgets import CKEditorUploadingWidget

User = get_user_model()

class CreateBlog(forms.ModelForm):
    class Meta:
        model = Blog

        fields = ['title', 'author', 'body']

        widgets = {
            'title': forms.TextInput(
                attrs={'class': 'form-control', 'style': 'width: 100%; height: 40px; font-size: 28px;', 'placeholder': '제목을 입력하세요.'}
            ),
            # 'author': forms.Select(
            #     attrs={'style': 'display: none;'}
            # ),
            'body': forms.CharField(widget=CKEditorUploadingWidget()),
        }

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        class_update_fields = ['username', 'password']
        for field_name in class_update_fields:
            self.fields[field_name].widget.attrs.update({
                'class': 'form-control'
            })


class SignupForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        class_update_fields = ['password1', 'password2']
        for field_name in class_update_fields:
            self.fields[field_name].widget.attrs.update({
                'class': 'form-control'
            })

    class Meta:
        model = User
        fields = (
            'username',
            'password1',
            'password2',
        )
        widgets = {
            'username': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
        }