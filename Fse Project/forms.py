from django import forms
from .models import uploadcode

class uploadcodeform(forms.ModelForm):
    class Meta:
        model=uploadcode
        fields = ['file']
        