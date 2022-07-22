from django import forms
from .models import football

class teamform (forms.ModelForm):
    class Meta:
        model=football
        fields=['name','disc','year','img']

