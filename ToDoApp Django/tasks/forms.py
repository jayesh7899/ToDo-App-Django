from django import forms
from django.forms import ModelForm
from .models import*




class TaskForm(forms.ModelForm):
    title=forms.CharField(widget=forms.TextInput(attrs={'Placeholder':'Add new task....'}))
    
    class Meta:

        model=task
        fields='__all__'