from .models import Meal
from django import forms
from django_summernote.widgets import SummernoteWidget


class MealForm(forms.ModelForm):
    class Meta:
        model = Meal
        fields = "__all__"
        widgets = {
            'recipe': SummernoteWidget(attrs={'summernote': {'width': '100%'}}),
        }
