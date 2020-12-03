from django import forms

from django.contrib.auth.password_validation import validate_password

from users.models import User


class SignUpForm(forms.ModelForm):

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'type': 'password',
                'name': 'passwordsss',
                'id': 'id_password',
                'class': 'form_input',
                'placeholder': 'Пароль'
            }
        ),
        validators=[validate_password]
        )

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'phone', 'userpic', 'password')
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'type': 'text',
                    'name': 'first_name',
                    'id': 'id_first_name',
                    'class': 'form_input',
                    'placeholder': 'Имя'
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'type': 'text',
                    'name': 'first_name',
                    'id': 'id_last_name',
                    'class': 'form_input',
                    'placeholder': 'Фамилия'
                }
            ),
            'username': forms.TextInput(
                attrs={
                    'type': 'text',
                    'name': 'username',
                    'id': 'id_username',
                    'class': 'form_input',
                    'placeholder': 'Имя пользователя'
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'type': 'email',
                    'name': 'email',
                    'id': 'id_email',
                    'class': 'form_input',
                    'placeholder': 'Электронная почта'
                }
            ),
            'phone': forms.TextInput(
                attrs={
                    'type': 'text',
                    'name': 'phone',
                    'id': 'id_phone',
                    'class': 'form_input',
                    'placeholder': 'Телефон'
                }
            ),
            'userpic': forms.FileInput(
                attrs={
                    'type': 'file',
                    'id': 'id_file',
                    'name': 'file',
                    'class': 'form_file'
                }
            ),
        
        }


class EditProfileForm(SignUpForm):

    def __init__(self, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.fields.pop('password')

    class Meta(SignUpForm.Meta):

        model = User
