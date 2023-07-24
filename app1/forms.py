from django import forms
from .models import Hotel, box
from django.utils import timezone
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class HotelForm(forms.ModelForm):
    class Meta:
        model = Hotel
        fields = ['name', 'hotel_Main_Img']

class BoxForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['box_pub_date'].initial = timezone.now()
    class Meta:
        model = box
        fields = ['box_title', 'box_image', 'box_price', 'box_adress', 'box_pub_date']
        widgets = {
            'box_title': forms.TextInput(attrs={'class': 'form-input'}),
            #'box_image': forms.ImageField,
            'box_adress': forms.TextInput(attrs={'class': 'form-input'}),
            #'box_pub_date': forms.DateTimeField(auto_now=True)
        }

class RegisterUserForm(UserCreationForm):

    username = forms.CharField(label="Логин", widget=forms.TextInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label="Логин", widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label="Логин", widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User 
        fields = ('username', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-input'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-input'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-input'}),
        }

class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label="Логин", widget=forms.TextInput(attrs={'class': "form-input"}))
    password = forms.CharField(label="Логин", widget=forms.PasswordInput(attrs={'class': "form-input"}))