from django import forms
from .models import Goat

class GoatForm(forms.ModelForm):
    class Meta:
        model = Goat
        fields = ['tag_no', 'name', 'breed', 'dob', 'gender', 'weight', 'health_status', 'location', 'status', 'sire_id', 'dam_id']
        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date'}),
        }


