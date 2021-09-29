from django import forms
from .models import Message


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control not-dark'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control not-dark'}))


class ContactForm(forms.ModelForm):
    class Meta:
        model = Message
        exclude = ('timestamp',)
        widgets = {
            'name': forms.TextInput(attrs={'class': 'sm-form-control border-form-control', 'placeholder': '姓名'}),
            'email': forms.EmailInput(
                attrs={'class': 'email sm-form-control border-form-control', 'placeholder': '電子信箱'}),
            'phone': forms.TextInput(attrs={'class': 'sm-form-control border-form-control', 'placeholder': '聯絡電話'}),
            'subject': forms.TextInput(attrs={'class': 'sm-form-control border-form-control', 'placeholder': '主旨'}),
            'content': forms.Textarea(attrs={'class': 'sm-form-control border-form-control', 'placeholder': '您想說什麼？'}),
        }
