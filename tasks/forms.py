from django import forms
from django.forms import ModelForm

from .models import *

class TaskForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Add new task . . . ','class':'form-control','style':'margin-bottom:10px'}))
    complete = forms.CharField(widget=forms.CheckboxInput({'class':'form-check-input','style':'margin-bottom:20px'}))
    class Meta:
        model = Task
        fields = '__all__'