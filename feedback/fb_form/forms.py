from django import forms
from .models import fb_form

class fb_form_Form(forms.ModelForm):
    class Meta:
        model= fb_form
        exclude=[]
