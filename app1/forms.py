from django import forms
from .models import Hotel, box
from django.utils import timezone

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

